import cv2
import numpy as np


class AddNoise:
    def __init__(self):
        self.noise_status = 1
        
    def add_noise(self, image, noise_value):
        """
        Bu fonksiyon, görüntüye gürültü ekler.
        noise_value değeri 30 ile 120 arasında verilebilir.
        """
        try:
            noise = np.random.normal(0, noise_value, image.shape)
            noisy_image = np.clip(image + noise, 0, 255)
            return self.noise_status, noisy_image.astype(np.uint8)
        except Exception as e:
            self.noise_status = 0
            return self.noise_status, e