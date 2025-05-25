import subprocess

def open_cmd_window(command):
    """Mở cửa sổ CMD mới và chạy lệnh"""
    subprocess.Popen(f"start cmd /K {command}", shell=True)

def main():
    # Nhập link video TikTok từ người dùng
    link = input("Nhập link video TikTok: ")

    # Câu lệnh sẽ chạy script của bạn với link đã nhập
    command = f"123.py {link}"

    # Chạy 100 tab CMD
    for _ in range(10):
        open_cmd_window(command)

if __name__ == "__main__":
    main()
