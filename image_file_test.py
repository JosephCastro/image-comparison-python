import unittest
from image_file import ImageFile


class ImageFileTestCase(unittest.TestCase):

    test_samples = [
        ('a1.jpg', 'a1.jpg', 0),
        ('a1.jpg', 'a2.jpg', 249),
        ('c2.jpg', 'c3.jpg', 31),
        ('b1.jpg', 'b2.jpg', 95),
        ('a1.jpg', 'b2.jpg', 423)

    ]

    def test_same_image(self):
        sample_dir = 'samples/'
        for data in self.test_samples:
            image_1 = ImageFile(sample_dir + data[0])
            image_2 = ImageFile(sample_dir + data[1])

            value = int(image_1.comparison(image_2))
            self.assertEqual(value, data[2])

    def test_generate_thumbnail(self):

        image = ImageFile('samples/a1.jpg')
        self.assertEqual(image.image.width, 300)
        self.assertEqual(image.image.height, 300)

        image = ImageFile.generate_thumbnail(image.image)
        self.assertEqual(image.width, 128)
        self.assertEqual(image.height, 128)
