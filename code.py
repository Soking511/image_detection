import os
import cv2
from detection import detect_objects
from paths import net, folders_path, image_extensions, classfile_path

# Main process function
def process_images():
    image_paths = []
    for folder in folders_path:
        if os.path.exists(folder):
            for f in os.listdir(folder):
                if f.lower().endswith(image_extensions):
                    image_paths.append(os.path.join(folder, f))

    if not image_paths:
        print("No images found for processing.")
        return

    processed_dir = 'photos/uploads/processed'
    os.makedirs(processed_dir, exist_ok=True)

    # Process each image
    for image_path in image_paths:
        img = cv2.imread(image_path)
        if img is None:
            print(f"Unable to read image: {image_path}")
            continue

        processed_image = detect_objects(img, net, classfile_path)
        cv2.imshow('Processed Image', processed_image)
        cv2.waitKey(0)

        processed_filename = os.path.join(processed_dir, f'processed_{os.path.basename(image_path)}')
        cv2.imwrite(processed_filename, processed_image)
        print(f"Processed image saved to: {processed_filename}")

    cv2.destroyAllWindows()

# Run the main process
if __name__ == "__main__":
    process_images()
