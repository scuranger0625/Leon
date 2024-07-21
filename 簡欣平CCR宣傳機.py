import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# 設置Chrome選項
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--start-maximized")

# 使用ChromeDriverManager安裝驅動並初始化WebDriver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

# 打開目標網頁
driver.get("https://www.youtube.com/watch?v=3o8GqDGf2co")

try:
    while True:
        # 等待30秒
        time.sleep(30)
        # 刷新頁面
        driver.refresh()
except KeyboardInterrupt:
    # 當用戶中斷程序時，關閉瀏覽器
    driver.quit()



