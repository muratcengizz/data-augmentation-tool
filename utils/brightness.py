import cv2
import numpy as np

class AdjustBrightness:
    def __init__(self):
        self.brightness_status = 1
    
    def adjust_brightness(self, image, delta):
        """
        Bu fonksiyon, görselin parlaklığını arttırır.
        delta değeri 5 ile 50 arasında verilebilir.
        """
        try:
            hsv_image = cv2.cvtColor(src=image, code=cv2.COLOR_BGR2HSV)
            hsv_image[:,:,2] = np.clip(hsv_image[:,:,2] + delta * 255, 0, 255)
            brightness_image = cv2.cvtColor(src=hsv_image, code=cv2.COLOR_HSV2BGR)
            return self.brightness_status, brightness_image
        except Exception as e:
            self.brightness_status = 0
            return self.brightness_status, e