import cv2
import numpy as np

class AdjustSaturation:
    def __init__(self):
        self.saturation_status = 1
        
    def adjust_saturation(self, image, delta):
        """
        Bu fonksiyon, görselin doygunluğunu (koyuluğunu) arttırır.
        delta değeri 5 ile 50 arasında verilebilir.
        """
        try:
            hsv_image = cv2.cvtColor(src=image, code=cv2.COLOR_BGR2HSV)
            hsv_image[:,:,1] = np.clip(hsv_image[:,:,1] + delta * 255, 0, 255)
            saturation_image = cv2.cvtColor(src=hsv_image, code=cv2.COLOR_HSV2BGR)
            return self.saturation_status, saturation_image
        except Exception as e:
            self.saturation_status = 0
            return self.saturation_status, e