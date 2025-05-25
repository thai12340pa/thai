import subprocess

def open_cmd_window(command):
    """Mở cửa sổ CMD mới và chạy lệnh"""
    subprocess.Popen(f"start cmd /K {command}", shell=True)

def main():
    # Nhập link video TikTok từ người dùng
    link = input("Nhập link video TikTok: ")

    # Nhập số lượng tab CMD mà người dùng muốn mở
    try:
        num_tabs = int(input("Nhập số lượng tab CMD muốn mở: "))
    except ValueError:
        print("Số lượng tab phải là một số nguyên.")
        return

    # Câu lệnh sẽ chạy script của bạn với link đã nhập
    command = f"python 123.py {link}"

    # Mở số tab CMD mà người dùng yêu cầu
    for _ in range(num_tabs):
        open_cmd_window(command)

if __name__ == "__main__":
    main()
