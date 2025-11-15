import cv2
import numpy as np
import subprocess
from config import CAMERA_RESOLUTION

def capture_frame():
    """
    Capture a single frame using libcamera.
    Returns a numpy array (BGR image) compatible with OpenCV.
    """
    width, height = CAMERA_RESOLUTION

    # Use libcamera-still to capture an image to a temporary file
    tmp_file = "/tmp/libcamera_capture.jpg"
    cmd = [
        "libcamera-still",
        "-o", tmp_file,
        "--width", str(width),
        "--height", str(height),
        "--nopreview",
        "-n"  # no preview
    ]
    subprocess.run(cmd, check=True)

    # Read the captured image with OpenCV
    frame = cv2.imread(tmp_file)
    if frame is None:
        raise RuntimeError("Failed to capture image with libcamera")
    return frame

def show_frame(frame, window_name="PiGPTBot Camera"):
    """
    Display a frame in a window (for debugging).
    """
    cv2.imshow(window_name, frame)
    cv2.waitKey(1)
