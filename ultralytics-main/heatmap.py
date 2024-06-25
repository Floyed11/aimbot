import cv2

from ultralytics import YOLO, solutions

name = "yolov8s_5"

model = YOLO(f"aimbot/models/{name}.pt")  # YOLOv8 custom/pretrained model

im0 = cv2.imread("aimbot/pic_tests/image.png")  # path to image file
h, w = im0.shape[:2]  # image height and width

# Heatmap Init
heatmap_obj = solutions.Heatmap(
    colormap=cv2.COLORMAP_PARULA,
    view_img=True,
    shape="circle",
    classes_names=model.names,
)

results = model.track(im0, persist=True)
# im0 = heatmap_obj.generate_heatmap(im0, tracks=results)
# cv2.imwrite("ultralytics_output.png", im0)
if results and hasattr(results[0].boxes, 'id') and results[0].boxes.id is not None:
    im0 = heatmap_obj.generate_heatmap(im0, tracks=results)
    cv2.imwrite(f"aimbot/pic_heatmap/{name}.png", im0)

else:
    print("No valid tracks found.")