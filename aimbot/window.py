from tkinter import Tk, Label
from PIL import Image, ImageTk
import tkinter as tk
import os

class Window:
    def __init__(self):
        # 创建Tkinter窗口
        self.time = 0.1
        self.root = tk.Tk()
        self.root.geometry("800x450")
        self.root.title("Aimbot")
        self.root.attributes("-topmost", True)

        self.index = 0

        current_file_path = os.path.abspath(__file__)
        current_dir = os.path.dirname(current_file_path)
        save_dir = "pic_predicts"
        self.image_folder = os.path.join(current_dir, save_dir)

        self.label = tk.Label(self.root)
        self.label.pack()
        # 开始更新图片
        self.start_updating()

    def get_latest_image_path(self):
        # 获取指定文件夹中所有图片文件
        image_files = [f for f in os.listdir(self.image_folder) if f.endswith(('.png', '.jpg', '.jpeg'))]
        # 根据文件的修改时间排序
        image_files.sort(key=lambda f: os.path.getmtime(os.path.join(self.image_folder, f)), reverse=True)
        if image_files:
            # 返回最新的图片文件路径
            return os.path.join(self.image_folder, image_files[self.index % len(image_files)])
        else:
            return None

    def start_updating(self):
        latest_image_path = self.get_latest_image_path()
        self.index=0
        if latest_image_path:
            # 加载图片并显示
            image = Image.open(latest_image_path)

            target_width = self.root.winfo_width()
            target_height = self.root.winfo_height()
            # 计算缩放比例
            ratio = min(target_width / image.width, target_height / image.height)
            # 根据比例计算新的图片尺寸
            new_size = (int(image.width * ratio), int(image.height * ratio))
            # 调整图片大小
            image = image.resize(new_size, Image.Resampling.LANCZOS)

            photo = ImageTk.PhotoImage(image)
            self.label.config(image=photo)
            self.label.image = photo  # 保持对photo的引用
        # 每秒更新一次
        self.root.after(int(self.time * 1000), self.start_updating)

if __name__ == "__main__":
    app = Window()
    app.root.mainloop()