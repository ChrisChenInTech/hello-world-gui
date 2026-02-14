"""
Hello World 桌面應用程式
使用 CustomTkinter 打造的現代化 Windows 桌面應用，
具備暗色模式、圓角按鈕與風格統一的對話框。
"""

import customtkinter as ctk


def center_window(window: ctk.CTk | ctk.CTkToplevel, width: int = 480, height: int = 320) -> None:
    """
    將視窗置於螢幕正中央。
    使用 winfo_screenwidth/height 取得螢幕尺寸後計算置中座標。
    """
    window.update_idletasks()
    screen_w = window.winfo_screenwidth()
    screen_h = window.winfo_screenheight()
    x = (screen_w - width) // 2
    y = (screen_h - height) // 2
    window.geometry(f"{width}x{height}+{x}+{y}")


def show_hello_dialog(parent: ctk.CTk) -> None:
    """
    顯示風格與主視窗一致的「Hello World」對話框。
    使用 CTkToplevel 實作，保持暗色主題與圓角樣式。
    """
    dialog = ctk.CTkToplevel(parent)
    dialog.title("訊息")
    # 設為暫時佔據焦點（類似 modal）
    dialog.transient(parent)
    dialog.grab_set()

    # 對話框尺寸與置中（相對於主視窗）
    dialog_width = 360
    dialog_height = 160
    dialog.geometry(f"{dialog_width}x{dialog_height}")
    dialog.resizable(False, False)

    # 置中：先取得主視窗位置，再讓對話框出現在主視窗中央
    parent.update_idletasks()
    px = parent.winfo_x()
    py = parent.winfo_y()
    pw = parent.winfo_width()
    ph = parent.winfo_height()
    dx = px + (pw - dialog_width) // 2
    dy = py + (ph - dialog_height) // 2
    dialog.geometry(f"+{dx}+{dy}")

    # 主訊息文字
    msg_label = ctk.CTkLabel(
        dialog,
        text="Hello World from Seattle!",
        font=ctk.CTkFont(size=16, weight="normal"),
        wraplength=dialog_width - 48,
    )
    msg_label.pack(pady=(32, 16), padx=24, fill="x")

    def on_ok() -> None:
        dialog.grab_release()
        dialog.destroy()

    ok_btn = ctk.CTkButton(
        dialog,
        text="確定",
        width=120,
        corner_radius=8,
        command=on_ok,
    )
    ok_btn.pack(pady=(0, 24))

    # 點擊確定或關閉視窗時釋放 grab
    dialog.protocol("WM_DELETE_WINDOW", on_ok)


def main() -> None:
    # 設定外觀：暗色模式
    ctk.set_appearance_mode("dark")
    # 可選：設定預設色彩主題（藍色系，與暗色搭配佳）
    ctk.set_default_color_theme("blue")

    # 建立主視窗
    win = ctk.CTk()
    win.title("Hello World 應用程式")
    win_width = 480
    win_height = 320
    win.geometry(f"{win_width}x{win_height}")
    win.resizable(True, True)
    center_window(win, win_width, win_height)

    # 中央圓角按鈕
    btn = ctk.CTkButton(
        win,
        text="點擊測試",
        font=ctk.CTkFont(size=16, weight="bold"),
        width=200,
        height=48,
        corner_radius=24,
        command=lambda: show_hello_dialog(win),
    )
    btn.place(relx=0.5, rely=0.5, anchor="center")

    win.mainloop()


if __name__ == "__main__":
    main()
