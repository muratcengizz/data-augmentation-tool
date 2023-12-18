



Algoritma:

Utils dizini altında ki modüller frame üzerinde çeşitli değişiklikler yapar. Ve bu modüller run.py içerisinde tetiklenir.
Kullanıcı parametrelere run.py içerisinde ki DataAugmentation() sınıfını çağırırken karar verir. Örneğin,

instance = DataAugmentation(video=False, 
                            rotation_range=20,
                            hue_range=50, 
                            brightness_range=40, 
                            saturation_range=40, 
                            noise_range=100)


"""
        RotateImage sınıfı, görseli saat yönünün tersine doğru döndürür.
        angle değeri 15 ile 60 arasında verilebilir.
"""

"""
        AdjustBrightness sınıfı, görselin parlaklığını arttırır.
        delta değeri 5 ile 50 arasında verilebilir.
"""

"""
        AdjustSaturation sınıfı, görselin doygunluğunu (koyuluğunu) arttırır.
        delta değeri 5 ile 50 arasında verilebilir.
"""

"""
        AddNoise sınıfı, görüntüye gürültü ekler.
        noise_value değeri 30 ile 120 arasında verilebilir.
"""

"""
        AdjustHue sınıfı, görselin renk tonunu değiştirir.
        delta değeri 20 ile 100 aralığında verilebilir.
"""


Mesela, veri çoğaltma işlemi sırasında frame'lere gürültü eklemek istemiyorsak tek yapmamız gereken DataAugmentation() sınıfına parametre girerken noise_range girmemek.