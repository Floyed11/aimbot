# 项目指南

## Aimbot启动方法

在项目主目录aimbot下执行以下命令

    cd ./aimbot
    python3 target_detect.py

主要可选参数：

    --modelpath 模型路径，可以为aimbot/aimbot目录下的所有权重文件
    --conf 置信度阈值，可以根据模型选择
    --iou iou阈值
    --time 间隔时间，单位为秒

## 测试数据集及模型测试方法

对于yolov8模型，数据集在aimbot/ultralytics-main/ultralytics/cfg/datasets下，可以用cs.yaml调用。

测试模型需要在aimbot/ultralytics-main目录下执行以下命令

    python3 val.py

可以根据需要修改`YOLO()`内的权重路径。

对于yolov5模型，数据集在aimbot/yolov5-main/data下，可以用data.yaml调用。

测试模型需要在aimbot/yolov5-main目录下执行以下命令

    python3 val.py --weights models/yolov5s_20.pt --data ./data/data.yaml --imgsz 640

其中`--weights`为权重路径，可以调整为需要的模型权重，`--data`为数据集路径，`--imgsz`为图片尺寸。



