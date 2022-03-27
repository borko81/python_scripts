from PIL import Image

FILE = "work_with_images/img.jpg"


class LoadImg:
    def __init__(self, img: str) -> None:
        self.img = img

    def load_img(self):
        return Image.open(self.img)

    def convert_size(self, new_w, new_h):
        new_img = self.load_img().resize((new_w, new_h), Image.ANTIALIAS)
        return new_img


if __name__ == "__main__":
    img = LoadImg(FILE)
    w, h = img.load_img().size
    new_img = img.convert_size(w // 2, h // 2)
    new_img.show()
