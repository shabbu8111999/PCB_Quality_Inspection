def calculate_center(x1, y1, x2, y2):
    """
    Calculate center point of a bounding box
    """
    cx = int((x1 + x2) / 2)
    cy = int((y1 + y2) / 2)
    return cx, cy


def assess_severity(x1, y1, x2, y2):
    """
    Simple severity estimation based on defect area
    """
    area = (x2 - x1) * (y2 - y1)

    if area > 5000:
        return "High"
    elif area > 2000:
        return "Medium"
    else:
        return "Low"
