"""
使用 PyInstaller 將 main.py 打包成單一 .exe 的腳本。
執行方式：python build.py
產出位置：dist/ 資料夾內的 .exe 檔。
"""

import subprocess
import sys


def main() -> None:
    # PyInstaller 參數說明：
    #   --onefile      : 打包成單一執行檔
    #   --windowed     : 不顯示命令列視窗（適合 GUI）
    #   --name         : 輸出的 .exe 檔名
    #   --clean        : 清理暫存後再打包
    cmd = [
        sys.executable,
        "-m",
        "PyInstaller",
        "--onefile",       # 單一 .exe
        "--windowed",      # 無 console 視窗
        "--name=HelloWorldApp",
        "--clean",
        "main.py",
    ]
    subprocess.run(cmd, check=True)
    print("Build completed successfully. Executable located at: dist/HelloWorldApp.exe")


if __name__ == "__main__":
    main()
