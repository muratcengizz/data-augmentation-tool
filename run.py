import os
import cv2
import uuid
from utils.rotate_image import RotateImage
from utils.hue import AdjustHue
from utils.brightness import AdjustBrightness
from utils.saturation import AdjustSaturation
from utils.noise import AddNoise


class DataAugmentation:
    def __init__(self, video=False, rotation_range=0, exposure_range=0, hue_range=0, brightness_range=0, saturation_range=0, noise_range=0):
        self.video = video
        self.rotation_range = rotation_range
        self.hue_range = hue_range
        self.brightness_range = brightness_range
        self.saturation_range = saturation_range
        self.noise_range = noise_range
        
        self.rotate_image = RotateImage()
        self.adjust_hue = AdjustHue()
        self.adjust_brightness = AdjustBrightness()
        self.adjust_saturation = AdjustSaturation()
        self.add_noise = AddNoise()
        
        self.DEFAULT_IMAGES_DIR = os.path.join("data", "default_images")
        self.AUGMENTED_IMAGES_DIR = os.path.join("data", "augmented_images")
        self.VIDEOS_DIR = os.path.join("data", "videos")
    
    
    def process(self):
        if self.video == False:
            images = os.listdir(path=self.DEFAULT_IMAGES_DIR)
            for image in images:
                image_name = image.split(".")[0]
                image = cv2.imread(filename=os.path.join(self.DEFAULT_IMAGES_DIR, image))
                
                
                if self.rotation_range != 0:
                    rotate_image_status, rotated_image = self.rotate_image.rotate_image(image=image, angle=self.rotation_range)
                    if rotate_image_status == 1:
                        imwrite = cv2.imwrite(filename=f"{self.AUGMENTED_IMAGES_DIR}\\{image_name}_rotated.jpg", img=rotated_image)
                    else:
                        print(rotated_image)
                
                if self.hue_range != 0:
                    hue_status, hue_image = self.adjust_hue.adjust_hue(image=image, delta=self.hue_range)
                    if hue_status == 1:
                        imwrite = cv2.imwrite(filename=f"{self.AUGMENTED_IMAGES_DIR}\\{image_name}_hue.jpg", img=hue_image)
                    else:
                        print(hue_image)
                
                if self.brightness_range != 0:
                    brightness_status, brightness_image = self.adjust_brightness.adjust_brightness(image=image, delta=self.brightness_range)
                    if brightness_status == 1:
                        imwrite = cv2.imwrite(filename=f"{self.AUGMENTED_IMAGES_DIR}\\{image_name}_brightness.jpg", img=brightness_image)
                    else:
                        print(hue_image)
                
                if self.saturation_range != 0:
                    saturation_status, saturation_image = self.adjust_saturation.adjust_saturation(image=image, delta=self.saturation_range)
                    if saturation_status == 1:
                        imwrite = cv2.imwrite(filename=f"{self.AUGMENTED_IMAGES_DIR}\\{image_name}_saturation.jpg", img=saturation_image)
                    else:
                        print(saturation_image)
                
                if self.noise_range != 0:
                    noise_status, noisy_image = self.add_noise.add_noise(image=image, noise_value=self.noise_range)
                    if noise_status == 1:
                        imwrite = cv2.imwrite(filename=f"{self.AUGMENTED_IMAGES_DIR}\\{image_name}_noisy.jpg", img=noisy_image)
                    else:
                        print(noisy_image)
        
        elif self.video:
            videos = os.listdir(path=self.VIDEOS_DIR)
            for video in videos:
                unique_name = uuid.uuid1()
                video = cv2.VideoCapture(f"{self.VIDEOS_DIR}\\{video}")
                
                while True:
                    retval, image = video.read()
                    if not retval: exit()
                    
                    
                    if self.rotation_range != 0:
                        rotate_image_status, rotated_image = self.rotate_image.rotate_image(image=image, angle=self.rotation_range)
                        if rotate_image_status == 1:
                            imwrite = cv2.imwrite(filename=f"{self.AUGMENTED_IMAGES_DIR}\\{unique_name}_rotated.jpg", img=rotated_image)
                        else:
                            print(rotated_image)
                
                    if self.hue_range != 0:
                        hue_status, hue_image = self.adjust_hue.adjust_hue(image=image, delta=self.hue_range)
                        if hue_status == 1:
                            imwrite = cv2.imwrite(filename=f"{self.AUGMENTED_IMAGES_DIR}\\{unique_name}_hue.jpg", img=hue_image)
                        else:
                            print(hue_image)
                
                    if self.brightness_range != 0:
                        brightness_status, brightness_image = self.adjust_brightness.adjust_brightness(image=image, delta=self.brightness_range)
                        if brightness_status == 1:
                            imwrite = cv2.imwrite(filename=f"{self.AUGMENTED_IMAGES_DIR}\\{unique_name}_brightness.jpg", img=brightness_image)
                        else:
                            print(hue_image)
                    
                    if self.saturation_range != 0:
                        saturation_status, saturation_image = self.adjust_saturation.adjust_saturation(image=image, delta=self.saturation_range)
                        if saturation_status == 1:
                            imwrite = cv2.imwrite(filename=f"{self.AUGMENTED_IMAGES_DIR}\\{unique_name}_saturation.jpg", img=saturation_image)
                        else:
                            print(saturation_image)
                    
                    if self.noise_range != 0:
                        noise_status, noisy_image = self.add_noise.add_noise(image=image, noise_value=self.noise_range)
                        if noise_status == 1:
                            imwrite = cv2.imwrite(filename=f"{self.AUGMENTED_IMAGES_DIR}\\{unique_name}_noisy.jpg", img=noisy_image)
                        else:
                            print(noisy_image)
        print("Tamamlandı.")        
        
instance = DataAugmentation(video=False, 
                            rotation_range=20,
                            hue_range=50, 
                            brightness_range=40, 
                            saturation_range=40, 
                            noise_range=100)

instance.process()