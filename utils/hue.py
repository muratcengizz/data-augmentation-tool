import cv2


class AdjustHue:
    def __init__(self):
        self.adjust_hue_status = 1
    
    def adjust_hue(self, image, delta):
        """
        Bu fonksiyon, görselin renk tonunu değiştirir.
        delta değeri 20 ile 100 aralığında verilebilir.
        """
        try:
            hsv_image = cv2.cvtColor(src=image, code=cv2.COLOR_BGR2HSV)
            hsv_image[:,:, 0] = (hsv_image[:,:,0] + delta) % 180
            adjust_image = cv2.cvtColor(src=hsv_image, code=cv2.COLOR_HSV2BGR)
            return self.adjust_hue_status, adjust_image
        except Exception as e:
            self.adjust_hue_status = 0
            return self.adjust_hue_status, e