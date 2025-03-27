import cv2
import numpy as np
import pyautogui
import time
import os

# 參數設定
record_seconds = 3000000  # 錄製時間（秒）
fps = 20.0  # 每秒幾格畫面
screen_size = pyautogui.size()  # 獲取螢幕解析度
desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
output_path = os.path.join(desktop_path, "螢幕錄影.mp4")

# 建立影片寫入器（指定格式、編碼器）
fourcc = cv2.VideoWriter_fourcc(*"mp4v")  # 使用 mp4 格式
out = cv2.VideoWriter(output_path, fourcc, fps, screen_size)

print(f"開始錄製，將持續 {record_seconds} 秒...")
start_time = time.time()

while True:
    # 擷取螢幕截圖
    img = pyautogui.screenshot()
    frame = np.array(img)  # 轉換為 numpy 陣列
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)  # 轉換色彩格式
    out.write(frame)

    # 檢查是否錄完指定時間
    if time.time() - start_time > record_seconds:
        break

print("錄製完成，影片已儲存至桌面：", output_path)
out.release()
cv2.destroyAllWindows()
