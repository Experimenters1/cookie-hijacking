import json
import tkinter as tk
from tkinter import filedialog, messagebox
import browser_cookie3
from selenium import webdriver

def load_cookies_from_json(file_path):
    with open(file_path, 'r') as f:
        return json.load(f)

def login_with_cookies():
    file_path = filedialog.askopenfilename(filetypes=[("JSON files", "*.json")])
    
    if file_path:
        try:
            cookies_json = load_cookies_from_json(file_path)
            browser = webdriver.Chrome()  # Hoặc sử dụng trình duyệt của bạn ở đây

            for cookie_json in cookies_json:
                browser.add_cookie(cookie_json)

            browser.get("https://www.youtube.com")
            
            # Kiểm tra xem đã đăng nhập thành công chưa bằng cách kiểm tra tiêu đề trang
            if "YouTube" in browser.title:
                messagebox.showinfo("Thành công", "Đăng nhập vào tài khoản YouTube thành công bằng cookies!")
            else:
                messagebox.showerror("Lỗi", "Không thể đăng nhập vào tài khoản YouTube bằng cookies!")
            
            browser.quit()
        except Exception as e:
            messagebox.showerror("Lỗi", f"Có lỗi xảy ra: {str(e)}")

def main():
    root = tk.Tk()
    root.title("Đăng nhập vào YouTube bằng Cookies")
    root.geometry("300x100")

    button = tk.Button(root, text="Chọn file cookies", command=login_with_cookies)
    button.pack(pady=20)

    root.mainloop()

if __name__ == "__main__":
    main()
