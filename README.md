# 🧾 Assignment 2: Automated Quality Inspection System for Manufacturing

## 📌 Project Title
PCB Defect Detection using Computer Vision

---

## 📖 Background
In manufacturing industries, products must be inspected for defects before packaging.  
Manual inspection is slow and can lead to human errors.  
This project demonstrates an automated visual inspection system using computer vision to detect defects on Printed Circuit Boards (PCBs).

---

## 🎯 Objective
The objective of this project is to develop a computer vision solution that:

- Analyzes PCB images  
- Detects and localizes defect regions  
- Classifies defect types with confidence scores  
- Outputs defect center coordinates and defect severity  

---

## 🧩 Chosen Manufactured Item
**Printed Circuit Board (PCB)**  

PCBs are chosen because:
- They have clear visual patterns  
- Defects are visible and well-defined  
- They are widely used in real manufacturing industries  

---

## 🐞 Defect Types Used
The dataset contains the following six PCB defect types:

1. Mouse Bite  
2. Spur  
3. Missing Hole  
4. Short Circuit  
5. Open Circuit  
6. Spurious Copper  

This satisfies the requirement of using at least three different defect types.

---

## Project Structure

pcb_quality_inspection/
│
├── pcb-defect-dataset/ # Dataset (not uploaded to GitHub)
│ └── data.yaml
│
├── samples/ # Sample images for submission
│ ├── images/
│ │ ├── defective_sample.jpg
│ │ └── non_defective_sample.jpg
│ │
│ └── annotations/
│ └── defective_sample.txt
│
├── src/
│ ├── train_model.py # Model training script
│ ├── detect_defects.py # Defect detection script
│ └── utils.py # Helper functions
│
├── main.py # Project entry point
├── requirements.txt # Dependencies
├── README.md # Documentation
└── .gitignore # Git ignore file

---

## 📊 Dataset Information

- **Dataset Source:** Kaggle PCB Defect Dataset  
- **Annotation Format:** YOLO  

The dataset includes:
- Training images  
- Validation images  
- Test images  

### ⚠️ Note
The full dataset is not included in this repository due to size limitations.  
Only a few sample images are provided for demonstration purposes.

---

## ⚙️ Technologies Used

- Python  
- OpenCV  
- Ultralytics YOLOv8  
- NumPy  

---

## 🛠️ How the System Works

- An input PCB image is given to the system  
- YOLOv8 analyzes the image  
- Defect regions are detected using bounding boxes  
- Each defect is classified with a confidence score  
- Center (x, y) pixel coordinates of defects are calculated  
- Defect severity is assessed based on defect area  

---

## 📤 Sample Output

Example output printed in the terminal:

```bash
  'defect': 'missing_hole',
  'confidence': 0.64,
  'center': (258, 421),
  'severity': 'Low'
```

- Bounding boxes are displayed on the image
- Defect type and confidence score are shown
- Pixel coordinates of defect center are calculated
- Severity is classified as Low / Medium / High

---

## 🖼️ Sample Images Included

- To meet assignment requirements:
    - 1 defective PCB image with annotation
    - 1 non-defective PCB image

- These are included inside the samples/ folder.

---

## 📝 Notes

- Full dataset is excluded from GitHub to follow best practices
- Only representative samples are included
- The focus is on building a working inspection pipeline, not achieving maximum accuracy

---

## ✅ Conclusion

This project successfully demonstrates an automated quality inspection system using computer vision. The system can detect, localize, and classify PCB defects with confidence and severity assessment, making it suitabe for real-world manufacturing inspection scenarios.