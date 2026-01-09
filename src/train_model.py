from ultralytics import YOLO


def train():
    model = YOLO("yolov8n.pt")

    model.train(
        data = "pcb-defect-dataset/data.yaml",
        epochs = 5,
        imgsz = 416,
        batch = 4
    )

if __name__ == "__main__":
    train()