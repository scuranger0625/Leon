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

# 目標網頁URL
target_url = "https://www.youtube.com/watch?v=qiRPSrFIPuM"

try:
    while True:
        # 獲取所有打開的窗口句柄
        window_handles = driver.window_handles
        found = False

        for handle in window_handles:
            # 切換到每個窗口
            driver.switch_to.window(handle)
            # 檢查當前窗口的URL
            if target_url in driver.current_url:
                found = True
                break

        if not found:
            # 如果沒有找到目標網頁，打開一個新分頁並導航到目標網頁
            driver.execute_script("window.open('{}', '_blank');".format(target_url))

        # 等待30秒
        time.sleep(30)
except KeyboardInterrupt:
    # 當用戶中斷程序時，關閉瀏覽器
    driver.quit()
