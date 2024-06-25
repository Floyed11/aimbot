from ultralytics import YOLO

model = YOLO("ultralytics/cfg/models/v8/yolov8s.yaml")
model = YOLO("yolov8s.pt")

# def freeze_model(trainer):
#     # Retrieve the batch data
#     model = trainer.model
#     print('Befor Freeze')
#     for k, v in model.named_parameters():
#         print('\t', k,'\t', v.requires_grad)
        
        
#     freeze = 10
#     freeze = [f'model.{x}.' for x in range(freeze)]  # layers to freeze
#     for k, v in model.named_parameters():
#         v.requires_grad = True  # train all layers
#         if any(x in k for x in freeze):
#             print(f'freezing {k}')
#             v.requires_grad = False
#     print('After Freeze')
#     for k, v in model.named_parameters():
#         print('\t', k,'\t', v.requires_grad)
        

# model.add_callback("on_pretrain_routine_start", freeze_model)


# train
model.train(data='cs.yaml',
            cache=False,
            epochs=1,
            batch=1,     
            imgsz=640,
            rect=False,
            resume=False,
            # device="mps",
            # freeze = [1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31,33,35,37,39],
            freeze=20,
            )

