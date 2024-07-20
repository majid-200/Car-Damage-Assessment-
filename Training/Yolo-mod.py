# import YOLO model
from ultralytics import YOLO

# Load a model
model = YOLO('yolov8s-cls.pt') # load a pretrained model (recommended for training)

# Train the model
if __name__ == '__main__':
    model.train(data='data', epochs=200)