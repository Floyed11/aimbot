from ultralytics import YOLO

if __name__ == '__main__':
    model = YOLO('./runs/detect/train6/weights/best.pt')
    images = './ultralytics/cfg/datasets/test/images/20_jpg.rf.c4fc41d31303f3dcf0daa59318031983.jpg'
    
    results = model(images,save=True)
    print(results)

