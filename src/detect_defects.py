from ultralytics import YOLO
import cv2
from src.utils import calculate_center, assess_severity


def detect_defects(image_path):
    model = YOLO("runs/detect/train/weights/best.pt")
    results = model(image_path)

    img = cv2.imread(image_path)

    for r in results:
        for box in r.boxes:
            x1, y1, x2, y2 = map(int, box.xyxy[0])
            conf = float(box.conf[0])
            cls = int(box.cls[0])
            name = model.names[cls]

            # used utils functions
            cx, cy = calculate_center(x1, y1, x2, y2)
            severity = assess_severity(x1, y1, x2, y2)

            print({
                "defect": name,
                "confidence": round(conf, 2),
                "center": (cx, cy),
                "severity": severity
            })

            cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.putText(
                img, name, (x1, y1 - 10),
                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2
            )

    cv2.imshow("Defect Detection", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    detect_defects("samples/images/defective_sample.jpg")
