from PIL import Image
import math
import operator


class ImageFile(object):

    def __init__(self, filepath):
        self.filepath = filepath
        self.image = Image.open(self.filepath)

    def comparison(self, image_file):
        thumbnail_1 = ImageFile.generate_thumbnail(self.image)
        thumbnail_2 = ImageFile.generate_thumbnail(image_file.image)

        return ImageFile.image_similar_histogram(thumbnail_1, thumbnail_2)

    @staticmethod
    def generate_thumbnail(
            image, size=(128, 128), stretch_to_fit=False, greyscale=False):
        if not stretch_to_fit:
            image.thumbnail(size, Image.ANTIALIAS)
        else:
            image = image.resize(size)

        if greyscale:
            image = image.convert("L")

        return image

    @staticmethod
    def image_similar_histogram(image_1, image_2):
        histogram_1 = image_1.histogram()
        histogram_2 = image_2.histogram()

        return math.sqrt(
            reduce(
                operator.add,
                list(map(lambda x, y: (x-y)**2, histogram_1, histogram_2))
            ) / len(histogram_1)
        )
