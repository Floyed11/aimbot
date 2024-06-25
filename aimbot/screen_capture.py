import os
import time
import cv2
import numpy as np
from matplotlib import pyplot as plt
from mss import mss
class ScreenCapture:
    def __init__(self):
        current_file_path = os.path.abspath(__file__)
        current_dir = os.path.dirname(current_file_path)
        save_dir = "pic_saves"
        self.save_path = os.path.join(current_dir, save_dir)

        self.sct = mss()
        self.monitor = self.sct.monitors[1]

        self.bound_box = {'left': self.monitor['width'] / 4, 'top': self.monitor['height'] / 4, 'width': self.monitor['width'] / 2, 'height': self.monitor['height'] / 2}


    def capScreen(self):
        sct_img = self.sct.grab(self.monitor)
        # sct_img = self.sct.grab(self.bound_box)

        sct_img = np.array(sct_img)         # HWC, and C==4
        sct_img = cv2.cvtColor(sct_img, cv2.COLOR_BGRA2BGR)     # 4 channels -> 3 channels
        return sct_img
    
    def savePic(self, img_array, img_name):
        cv2.imwrite(os.path.join(self.save_path, img_name), img_array)
        



def capScreen(mss_obj, bound_box):
    '''
    mss_obj: mss object
    bound_box: dict, 截图区域，eg.{'left': 0, 'top': 0, 'width': 1920, 'height': 1080}
    return: numpy_array
    (maybe add saves arg.)
    '''
    sct_img = mss_obj.grab(bound_box)
    sct_img = np.array(sct_img)         # HWC, and C==4
    sct_img = cv2.cvtColor(sct_img, cv2.COLOR_BGRA2BGR)     # 4 channels -> 3 channels
    return sct_img


def testTime():
    # mss_path = './saves/mss_saves'  # 截屏存储目录
    # if not os.path.exists(mss_path):
    #     os.mkdir(mss_path)

    # 获取当前文件的绝对路径
    current_file_path = os.path.abspath(__file__)

    # 获取当前文件所在的目录
    current_dir = os.path.dirname(current_file_path)

    # 指定要保存文件的子目录
    save_dir = "pic_saves"

    # 使用os.path.join连接目录，形成最终的保存路径
    mss_path = os.path.join(current_dir, save_dir)


    sct = mss()  # mss对象    
    bounding_box = sct.monitors[1]  # 截图区域，距离屏幕左上角距离，以及截屏宽高

    counter = 0
    img_name = '0.jpg'
    start = time.time()
    while True:
        sct_array = capScreen(sct, bounding_box)
        counter = counter + 1
        img_name = str(counter) + '.jpg'
        cv2.imwrite(os.path.join(mss_path, img_name), sct_array)
        print('save:', img_name, "path:", os.path.join(mss_path, img_name))
        if counter == 99:
            break

    end = time.time()
    print('time_cost:', end - start, 's')


def testPicFormat():
    sct = mss()
    bounding_box = {'left': 0, 'top': 0, 'width': 512, 'height': 256}
    img_array = capScreen(sct, bounding_box)        # img_array -> [256, 512, 4], this is HWC, need to be CHW


if __name__ == '__main__':
    sc = ScreenCapture()
    testTime()
    testPicFormat()
