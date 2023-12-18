import cv2



class RotateImage:
    def __init__(self):
        pass
    
    def rotate_image(self, image, angle):
        """
        Bu fonksiyon, görseli saat yönünün tersine doğru döndürür.
        angle değeri 15 ile 60 arasında verilebilir.
        """
        try:
            rotate_image_status = 1
            height, width = image.shape[:2]
            center = (width/2, height/2)
            rotation_matrix = cv2.getRotationMatrix2D(center=center, angle=angle, scale=1)
            rotated_image = cv2.warpAffine(src=image, M=rotation_matrix, dsize=(width, height))
            return rotate_image_status, rotated_image
            
        except Exception as e:
            rotate_image_status = 0
            return rotate_image_status, e
        


