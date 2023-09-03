from unittest import TestCase, main
from Testing.Exercise.project.mammal import Mammal
#from project.mammal import Mammal - С него тръгва Judge


class TestMammal(TestCase):

    def setUp(self):
        self.mammal = Mammal("John", "Dog", "Sound")

    def test_initializing(self):
        self.assertEqual("John", self.mammal.name)
        self.assertEqual("Dog", self.mammal.type)
        self.assertEqual("Sound", self.mammal.sound)
        self.assertEqual("animals", self.mammal._Mammal__kingdom)

    def test_sound_making(self):
        expected = f"{self.mammal.name} makes {self.mammal.sound}"
        self.assertEqual(expected, self.mammal.make_sound())

    def test_get_kingdom(self):
        self.assertEqual("animals", self.mammal.get_kingdom())

    def test_info(self):
        expected = f"{self.mammal.name} is of type {self.mammal.type}"
        self.assertEqual(expected, self.mammal.info())


if __name__ == '__main__':
    main()
