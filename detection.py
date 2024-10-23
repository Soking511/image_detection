import cv2
import os

# Load class names from the file
def class_names(classfile):
    if not os.path.exists(classfile):
        raise FileNotFoundError(f"Class names file not found: {classfile}")
    with open(classfile, 'rt') as f:
        return f.read().rstrip('\n').split('\n')

# Detect objects in the given image
def detect_objects(image, model, classfile, confidence_threshold=0.5):
    classnames = class_names(classfile)
    classIds, confs, bbox = model.detect(image, confThreshold=confidence_threshold)
    if classIds is None or confs is None or bbox is None:
      print("No objects detected.")
      return image  # Return the original image if no detections

    for classId, confidence, box in zip(classIds.flatten(), confs.flatten(), bbox):
        cv2.rectangle(image, box, color=(0, 255, 0), thickness=3)
        label = f"{classnames[classId-1]}: {confidence:.2f}"
        label_size, base_line = cv2.getTextSize(label, cv2.FONT_HERSHEY_SIMPLEX, 0.5, 1)
        top_left = (box[0], box[1] - label_size[1])
        bottom_right = (box[0] + label_size[0], box[1])
        cv2.rectangle(image, top_left, bottom_right, (255, 255, 255), cv2.FILLED)
        cv2.putText(image, label, (box[0], box[1] - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 1)

    return image
