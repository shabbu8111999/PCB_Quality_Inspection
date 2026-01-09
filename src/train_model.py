from ultralytics import YOLO


def train():
    model = YOLO("yolov8n.pt")

    model.train(
        data = "pcb-defect-dataset/data.yaml",
        epochs = 20,
        imgsz = 640,
        batch = 8
    )

if __name__ == "__main__":
    train()