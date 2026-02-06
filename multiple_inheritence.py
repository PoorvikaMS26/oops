# Parent Class 1
class Camera:
    def __init__(self, camera_quality):
        self.camera_quality = camera_quality

    def display_camera_details(self):
        print("Camera Quality:", self.camera_quality)


# Parent Class 2
class MusicPlayer:
    def __init__(self, sound_quality):
        self.sound_quality = sound_quality

    def display_music_details(self):
        print("Sound Quality:", self.sound_quality)


# Child Class (Multiple Inheritance)
class SmartPhone(Camera, MusicPlayer):
    def __init__(self, brand, camera_quality, sound_quality):
        super().__init__(camera_quality)
        MusicPlayer.__init__(self, sound_quality)
        self.brand = brand

    def display_smartphone_details(self):
        print("Smartphone Brand:", self.brand)
        self.display_camera_details()
        self.display_music_details()


# Create Object
phone1 = SmartPhone("vivo", "64 MP", "Dolby Atmos")

# Display Details
phone1.display_smartphone_details()