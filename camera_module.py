from picamera2 import Picamera2
import cv2
from config import CAMERA_RESOLUTION

camera = Picamera2()
camera_config = camera.create_preview_configuration(main={"size": CAMERA_RESOLUTION})
camera.configure(camera_config)
camera.start()

def capture_frame():
    """Capture a single frame from the camera."""
    frame = camera.capture_array()
    return frame

def show_frame(frame, window_name="PiGPTBot Camera"):
    cv2.imshow(window_name, frame)
    cv2.waitKey(1)
