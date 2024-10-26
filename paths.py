import cv2

folders_path = ['photos/images', 'photos/uploads/processed']
classfile_path = 'files/thing.names'
model_path = 'files/frozen_inference_graph.pb'
config_path = 'files/ssd_mobilenet_v3_large_coco_2020_01_14.pbtxt'
image_extensions = ('.png', '.jpg', '.jpeg', '.bmp', '.tiff')
image_paths = []
net = cv2.dnn_DetectionModel(model_path, config_path)
net.setInputSize(320, 320)
net.setInputScale(1.0 / 127.5)
net.setInputMean((127.5, 127.5, 127.5))
net.setInputSwapRB(True)

