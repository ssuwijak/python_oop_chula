class Camera:
    def take_photo(self):
        print("take a photo")

    def delete_photo(self):
        print("delete a photo")

    def browse(self):
        print("browse photo album")


class Phone:
    def call(self, number):
        print("call to tel_no {}".format(number))

    def send_sms(self, number, msg):
        print("send '{}' to tel_no {}".format(msg, number))


class MediaPlayer:
    def play_music(self):
        print("play music")

    def browse(self):
        print("browse media library")


class SmartPhone(Phone, Camera, MediaPlayer):
    pass


class SmartPhone2(Phone, MediaPlayer, Camera):
    pass


if __name__ == "__main__":
    s = SmartPhone()
    s.call("123456789")
    s.send_sms("987654321", "hello world")
    s.take_photo()
    s.delete_photo()
    s.play_music()
    s.browse()

    s2 = SmartPhone2()
    s2.browse()  # in case of same method name, it will use by order of the inherit classes
