from unittest import TestCase, main


class CatTester(TestCase):

    def setUp(self):
        self.cat = Cat("TestCat")

    def test_increased_size_after_eating(self):
        expected_size = self.cat.size + 1
        self.cat.eat()
        self.assertEqual(expected_size, self.cat.size)

    def test_cat_is_fed_after_eating(self):
        self.cat.eat()
        self.assertTrue(self.cat.fed)

    def test_cat_cannot_eat_if_is_already_fed(self):
        self.cat.eat()

        with self.assertRaises(Exception) as ex:
            self.cat.eat()

        self.assertEqual("Already fed.", str(ex.exception))

    def test_cat_cannot_fall_asleep_if_not_fed(self):
        with self.assertRaises(Exception) as ex:
            self.cat.sleep()

        self.assertEqual('Cannot sleep while hungry', str(ex.exception))

    def test_cat_cant_be_sleepy_after_sleeping(self):
        self.cat.eat()
        self.cat.sleep()
        self.assertFalse(self.cat.sleepy)


if __name__ == "__main__":
    main()


