from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os
import json
import glob

def get_chrome_cookies(url, profile_path):
    """
    Lấy cookie từ một profile cụ thể của Google Chrome.

    Args:
        url: URL của trang web.
        profile_path: Đường dẫn đến profile cần lấy cookies.

    Returns:
        Danh sách chứa các đối tượng cookie.
    """
    options = Options()
    options.add_argument(f"user-data-dir={profile_path}")
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    options.add_argument("--window-size=1920,1080")

    driver = webdriver.Chrome(options=options)
    driver.get(url)

    cookies = driver.get_cookies()
    driver.quit()

    return cookies

def get_all_profiles_cookies(url):
    """
    Lấy cookies từ tất cả các profiles trong Google Chrome.

    Args:
        url: URL của trang web.

    Returns:
        Dictionary chứa cookies theo profile.
    """
    username = os.getlogin()  # Hoặc sử dụng os.environ.get('USERNAME')
    chrome_profile_path = rf'C:\Users\{username}\AppData\Local\Google\Chrome\User Data'

    # Liệt kê tất cả các profiles
    profile_paths = glob.glob(os.path.join(chrome_profile_path, 'Profile *')) + [os.path.join(chrome_profile_path, 'Default')]
    all_cookies = {}

    for profile_path in profile_paths:
        profile_name = os.path.basename(profile_path)
        cookies = get_chrome_cookies(url, profile_path)
        if cookies:
            all_cookies[profile_name] = cookies

    return all_cookies

def main():
    url = "https://www.youtube.com/"
    all_cookies = get_all_profiles_cookies(url)
    if all_cookies:
        # Lưu tất cả cookies vào file all_cookies.json
        with open('all_cookies.json', 'w') as file:
            json.dump(all_cookies, file, indent=4)
        print("Cookies của tất cả profiles đã được lưu vào 'all_cookies.json'.")
    else:
        print("Không lấy được cookies từ bất kỳ profile nào.")

if __name__ == "__main__":
    main()
