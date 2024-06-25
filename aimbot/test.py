# # import Cocoa
# # import Quartz.CoreGraphics as CG
# # from PyObjCTools.AppHelper import NSApplicationMain, NSObject

# # class TransparentWindow(NSObject):
# #     def applicationDidFinishLaunching_(self, notification):
# #         # 创建一个无边框的窗口
# #         self.window = Cocoa.NSWindow.alloc().initWithContentRect_styleMask_backing_defer_(
# #             ((200.0, 300.0), (400.0, 200.0)),  # 窗口位置和大小
# #             Cocoa.NSWindowStyleMaskBorderless,  # 无边框
# #             Cocoa.NSBackingStoreBuffered,
# #             False
# #         )
# #         self.window.setOpaque_(False)  # 设置窗口为透明
# #         self.window.setBackgroundColor_(Cocoa.NSColor.clearColor())  # 设置背景色为透明
# #         self.window.setLevel_(Cocoa.NSFloatingWindowLevel)  # 窗口置顶
# #         self.window.makeKeyAndOrderFront_(None)  # 显示窗口

# #         # 创建一个自定义视图用于绘制矩形
# #         self.view = CustomView.alloc().initWithFrame_(((0, 0), (400, 200)))
# #         self.window.setContentView_(self.view)

# # class CustomView(Cocoa.NSView):
# #     def drawRect_(self, rect):
# #         # 设置矩形颜色为蓝色
# #         Cocoa.NSColor.blueColor().set()
# #         # 绘制矩形
# #         Cocoa.NSBezierPath.fillRect_(Cocoa.NSMakeRect(50, 50, 300, 100))

# # if __name__ == "__main__":
# #     app = NSApplication.sharedApplication()
# #     delegate = TransparentWindow.alloc().init()
# #     app.setDelegate_(delegate)
# #     NSApplicationMain([])
# import pygame

# # 初始化Pygame
# pygame.init()

# # 创建一个800x600的窗口
# screen = pygame.display.set_mode((640, 640))

# # 创建一个透明矩形
# transparent_rect = pygame.Surface((200, 100), pygame.SRCALPHA)
# transparent_rect.fill((255, 255, 255, 128))

# # 在窗口上绘制矩形
# screen.blit(transparent_rect, (300, 200))

# # 刷新窗口
# pygame.display.flip()

# # 游戏主循环
# running = True
# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False

# # 退出Pygame
# pygame.quit()
import tkinter as tk
from tkinter import PhotoImage, Label
from PIL import Image, ImageTk

# 创建Tkinter窗口
root = tk.Tk()
root.title("显示图片")

root.attributes("-topmost", True)

# 使用Pillow加载JPG图片
image_path = "/Users/linto/Documents/AI基础/aimbot/aimbot/runs/detect/predict/test_img.jpg"  # 替换为你的图片路径
image = Image.open(image_path)
photo = ImageTk.PhotoImage(image)

# 创建一个Label，显示图片
label = Label(root, image=photo)
label.pack()

# 进入Tkinter的主事件循环
root.mainloop()