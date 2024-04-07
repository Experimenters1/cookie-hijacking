from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os
import json

def get_chrome_cookies(url):
    """
    Lấy cookie từ trình duyệt Google Chrome ở chế độ headless và truy cập URL trên Windows, tự động lấy tên người dùng.

    Args:
        url: URL của trang web.

    Returns:
        Danh sách chứa các đối tượng cookie.
    """
    username = os.getlogin()  # Hoặc sử dụng os.environ.get('USERNAME')
    chrome_profile_path = rf'C:\Users\{username}\AppData\Local\Google\Chrome\User Data'

    options = Options()
    options.add_argument(f"user-data-dir={chrome_profile_path}")
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    options.add_argument("--window-size=1920,1080")

    driver = webdriver.Chrome(options=options)
    driver.get(url)

    cookies = driver.get_cookies()
    driver.quit()

    return cookies

def main():
    url = "https://www.youtube.com/"
    cookies = get_chrome_cookies(url)
    if cookies:
        # Lưu cookies vào file cookies.json
        with open('cookies.json', 'w') as file:
            json.dump(cookies, file, indent=4)
        print("Cookies đã được lưu vào 'cookies.json'.")
    else:
        print("Không lấy được cookies.")

if __name__ == "__main__":
    main()
