# Step 1: Import necessary libraries
import pandas as pd
import numpy as np
import yfinance as yf
from sklearn.preprocessing import MinMaxScaler
from keras.models import Sequential
from keras.layers import LSTM, Dense
import matplotlib.pyplot as plt

# Step 2: Download stock data
ticker = 'TSLA'
data = yf.download(ticker, start='2008-01-01', end='2024-06-07')

# Step 3: Data preprocessing
data = data[['Close']]
scaler = MinMaxScaler(feature_range=(0, 1))
scaled_data = scaler.fit_transform(data)

# Prepare the dataset for LSTM
train_size = int(len(scaled_data) * 0.8)
train_data, test_data = scaled_data[:train_size], scaled_data[train_size:]

def create_dataset(dataset, time_step=1):
    X, y = [], []
    for i in range(len(dataset)-time_step-1):
        a = dataset[i:(i+time_step), 0]
        X.append(a)
        y.append(dataset[i + time_step, 0])
    return np.array(X), np.array(y)

time_step = 60
X_train, y_train = create_dataset(train_data, time_step)
X_test, y_test = create_dataset(test_data, time_step)

# Reshape input to be [samples, time steps, features] which is required for LSTM
# The reshape is done to make sure the data has the correct shape expected by LSTM
X_train = np.reshape(X_train, (X_train.shape[0], X_train.shape[1], 1))
X_test = np.reshape(X_test, (X_test.shape[0], X_test.shape[1], 1))


# Step 4: Build and train the LSTM model
model = Sequential()
model.add(LSTM(50, return_sequences=True, input_shape=(time_step, 1)))
model.add(LSTM(50, return_sequences=False))
model.add(Dense(25))
model.add(Dense(1))

model.compile(optimizer='adam', loss='mean_squared_error')
model.fit(X_train, y_train, batch_size=1, epochs=1)

# Step 5: Make predictions
train_predict = model.predict(X_train)
test_predict = model.predict(X_test)

# Inverse transform to get the actual values
train_predict = scaler.inverse_transform(train_predict)
test_predict = scaler.inverse_transform(test_predict)
y_train = scaler.inverse_transform([y_train])
y_test = scaler.inverse_transform([y_test])

# Step 6: Evaluate the model
train_score = np.sqrt(np.mean(np.square(y_train[0] - train_predict[:,0])))
test_score = np.sqrt(np.mean(np.square(y_test[0] - test_predict[:,0])))
print(f'Train Score: {train_score:.2f} RMSE')
print(f'Test Score: {test_score:.2f} RMSE')

# Display tomorrow's closing price prediction (2024-06-08)
last_60_days = scaled_data[-60:]
# 將last_60_days轉換為二維陣列
last_60_days = np.array(last_60_days).reshape(-1, 1)
last_60_days = scaler.transform(last_60_days)

X_test_tomorrow = last_60_days.reshape(1, time_step, 1)
predicted_price_tomorrow = model.predict(X_test_tomorrow)
predicted_price_tomorrow = scaler.inverse_transform(predicted_price_tomorrow)
print(f"Predicted closing price for tomorrow (2024-06-08): ${predicted_price_tomorrow[0][0]:.2f}")

# Corrected Plotting
train_plot = np.empty_like(scaled_data)
train_plot[:, :] = np.nan
train_plot[time_step:len(train_predict)+time_step, :] = train_predict

test_plot = np.empty_like(scaled_data)
test_plot[:, :] = np.nan
test_plot[len(train_predict)+(time_step*2)+1:len(scaled_data)-1, :] = test_predict

# Plotting the results
plt.figure(figsize=(14, 7))
plt.plot(data.index, scaler.inverse_transform(scaled_data), label='Actual Prices')
plt.plot(data.index, train_plot, label='Training Predictions')
plt.plot(data.index, test_plot, label='Testing Predictions')
plt.xlabel('Date')
plt.ylabel('Price')
plt.title('Stock Price Prediction')
plt.legend()

# Add price text to the last data point
last_date = data.index[-1]
last_price = scaler.inverse_transform(scaled_data)[-1][0]
plt.text(last_date, last_price, f"${last_price:.2f}", fontsize=12, ha='right')

plt.show()


