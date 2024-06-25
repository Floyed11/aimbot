from ultralytics import YOLO

if __name__ == '__main__':
    model = YOLO('./runs/detect/train36/weights/best.pt')
    model.val(data='cs.yaml',
              split='val',
              imgsz=640,
              batch=1,
              save_json=True, # if you need to cal coco metrice
              project='runs/val',
              name='cs',
              )
