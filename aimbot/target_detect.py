import signal
import sys
import argparse
from ultralytics import YOLO
import time
from PIL import Image
import os
import threading
import pyautogui
from screen_capture import ScreenCapture
from window import Window


class yoloAimbot:

    def __init__(self, opt):
        self.time = 0.1

        self.modelpath = opt.modelpath
        self.conf = opt.conf
        self.iou = opt.iou
        self.img_size = opt.imgsz
        self.classes = opt.classes
        self.agnostic_nms = opt.agnostic_nms
        self.augment = opt.augment
        self.show = opt.show

        # self.bounding_box = {'left': 0, 'top': 0, 'width': 1920, 'height': 1080}
        
        self.aim_persons_center = []
        self.aim_persons_center_head = []
        # load model
        self.model = YOLO(self.modelpath)
        # self.model = attempt_load(self.weights, map_location=self.device)  # load FP32 model
        # self.model = self.model.to(self.device)
        # self.img_size = check_img_size(self.img_size, s=self.model.stride.max())  # check img_size
        # if self.half:
        #     self.model.half()  # to FP16

        # name and color
        # self.names = self.model.modules.names if hasattr(self.model, 'module') else self.model.names
        # self.colors = [[random.randint(0, 255) for _ in range(3)] for _ in range(len(self.names))]
        self.pic_cnt = 0
        self.pic_input_cnt = 0

        self.screenWidth, self.screenHeight = pyautogui.size()

        self.window = Window()
        self.window.time = self.time
        gui_thread = threading.Thread(target=self.run_aimbot)
        gui_thread.start()
        print("aimbot thread started.")   

        # mouse_thread = threading.Thread(target=self.moveMouse)
        # mouse_thread.start()
        # print("mouse thread started.")

        self.window.root.mainloop()

    
    def run_aimbot(self):
        self.run()
        # self.testFunction()


    def calculateDistance(self, xyxy):
        if len(xyxy) == 0:
            return 0, 0
        x1, y1, x2, y2 = xyxy
        x = int((x2 - x1) / 2 + x1)
        y = int((y2 - y1) / 2 + y1)
        return x, y

    def moveMouse(self, body_list, head_list):
        # body_list = self.aim_persons_center
        # head_list = self.aim_persons_center_head

        current_x, current_y = pyautogui.position()
        print("current mouse position:", current_x, current_y)
        targetxy = None
        if head_list:
            for head in head_list:
                dist = ((head[0] - current_x) ** 2 + (head[1] - current_y) ** 2) ** .5
                if not targetxy:
                    targetxy = (head, dist)
                else:
                    _, pre_dist = targetxy
                    if dist < pre_dist:
                        targetxy = (head, dist)
        elif body_list:
            for body in body_list:
                dist = ((body[0] - current_x) ** 2 + (body[1] - current_y) ** 2) ** .5
                if not targetxy:
                    targetxy = (body, dist)
                else:
                    _, pre_dist = targetxy
                    if dist < pre_dist:
                        targetxy = (body, dist)
        if targetxy:
            pyautogui.moveTo(targetxy[0][0], targetxy[0][1], duration=0.0)
            print("mouse moved to:", targetxy[0][0], targetxy[0][1])


    def run(self):

        sc = ScreenCapture()

        while True:
            cap_pic = sc.capScreen()
            self.pic_input_cnt += 1
            sc.savePic(cap_pic, f"input{self.pic_input_cnt}.jpg")
            # cap_pic = 'test_pics/test_img.jpg'

            source = cap_pic
            results = self.model.predict(source, conf=self.conf, iou=self.iou, imgsz=self.img_size, classes=self.classes,
                                         agnostic_nms=self.agnostic_nms, augment=self.augment, show=self.show, save=False)

            self.aim_persons_center = []
            self.aim_persons_center_head = []
            for i, r in enumerate(results):
                
                # im_bgr = r.plot()
                # im_rgb = Image.fromarray(im_bgr[..., ::-1])  # RGB-order PIL image

                # Save results to disk
                self.pic_cnt += 1
                filename = os.path.join(self.window.image_folder, f"results{self.pic_cnt}.jpg")
                r.save(filename=filename)

                if (not r.boxes):
                    continue
                xyxy = r.boxes.xyxy
                xyxyn = r.boxes.xyxyn
                cls = r.boxes.cls
                # print("xyxy:", xyxy)
                # print("xyxyn:", r.boxes.xyxyn)

                # 计算中心点
                for i in range(len(xyxy)):
                    x1_pixel = xyxyn[i][0] * self.screenWidth
                    y1_pixel = xyxyn[i][1] * self.screenHeight
                    x2_pixel = xyxyn[i][2] * self.screenWidth
                    y2_pixel = xyxyn[i][3] * self.screenHeight
                    # center_x, center_y = self.calculateDistance(xyxy[i])
                    center_x, center_y = self.calculateDistance([x1_pixel, y1_pixel, x2_pixel, y2_pixel])
                    self.aim_persons_center.append([center_x, center_y])
                    if int(cls[i]) == 1 or int(cls[i]) == 3:  # 特定类别的中心点
                        self.aim_persons_center_head.append([center_x, center_y])
            
            self.moveMouse(self.aim_persons_center, self.aim_persons_center_head)

            # time.sleep(self.time)




    def testFunction(self):
        sc = ScreenCapture()
        # cap_pic = sc.capScreen()
        cap_pic = 'test_pics/test_img.jpg'
        results = self.model.predict(
            cap_pic, conf=self.conf, show=self.show, save=False)

        aim_persons_center = []
        aim_persons_center_head = []
        for i, r in enumerate(results):
            
            # im_bgr = r.plot()
            # im_rgb = Image.fromarray(im_bgr[..., ::-1])  # RGB-order PIL image

            # # Show results to screen (in supported environments)
            # r.show()

            # Save results to disk
            self.pic_cnt += 1
            filename = os.path.join(self.window.image_folder, f"results{self.pic_cnt}.jpg")
            r.save(filename=filename)

            xyxy = r.boxes.xyxy
            cls = r.boxes.cls
            print("xyxy:", xyxy)

            # 计算中心点
            center_x, center_y = self.calculateDistance(xyxy[0])

            print("center_x, center_y:", center_x, center_y)
            aim_persons_center.append([center_x, center_y])
            if int(cls) == 1 or int(cls) == 3:  # 特定类别的中心点
                aim_persons_center_head.append([center_x, center_y])


def parseInit():
    parser = argparse.ArgumentParser()
    parser.add_argument('--modelpath', type=str,
                        default='models/best_30.pt', help='choose the model')
    parser.add_argument('--conf', type=float, default=0.1,
                        help='set confidence threshold')
    parser.add_argument('--iou', type=float, default=0.5,
                        help='IOU threshold for NMS')
    parser.add_argument('--imgsz', type=int, default=640,
                        help='set image size')
    parser.add_argument('--classes', nargs='+', type=int,
                        help='detect only these classes')
    parser.add_argument('--agnostic-nms', action='store_true',
                        help='activate agnostic NMS')
    parser.add_argument('--augment', action='store_true',
                        help='activate augmented TTA')
    parser.add_argument('--show', action='store_true', help='show detections')
    parser.add_argument('--time', type=float, default=0.1, help='predict time interval')
    opt = parser.parse_args()
    return opt


if __name__ == '__main__':
    signal.signal(signal.SIGINT, lambda x, y: sys.exit(0))

    opt = parseInit()
    aimbot = yoloAimbot(opt)
    print('yoloAimbot successfully created.')
    print("opt is set as:", opt)

    # aimbot.run()
    aimbot.testFunction()
