from unittest import TestCase, main
from project.second_hand_car import SecondHandCar  # Import the class from your module


class TestSecondHandCar(TestCase):
    def setUp(self):
        self.car1 = SecondHandCar("Toyota", "Sedan", 20000, 15000.0)
        self.car2 = SecondHandCar("Honda", "SUV", 30000, 18000.0)

    def test_price_setter(self):
        self.assertEqual(15000.0, self.car1.price)
        self.assertEqual(18000.0, self.car2.price)

    def test_mileage_setter(self):
        self.assertEqual(20000, self.car1.mileage)
        self.assertEqual(30000, self.car2.mileage)

    def test_set_promotional_price(self):
        car = SecondHandCar("Toyota", "Sedan", 20000, 15000.0)

        result = car.set_promotional_price(14000.0)
        self.assertEqual(result, 'The promotional price has been successfully set.')
        self.assertEqual(car.price, 14000.0)

        with self.assertRaises(ValueError):
            car.set_promotional_price(16000.0)

        with self.assertRaises(ValueError):
            car.set_promotional_price(15000.0)

    def test_price_mileage_constraints_car1(self):
        with self.assertRaises(ValueError):
           SecondHandCar("Toyota", "Sedan", 50, 15000.0)

        with self.assertRaises(ValueError):
            SecondHandCar("Toyota", "Sedan", 20000, 0.5)

    def test_need_repair(self):
        car = SecondHandCar("Toyota", "Sedan", 20000, 15000.0)

        result = car.need_repair(700, "Replace spark plugs")
        self.assertEqual(result, 'Price has been increased due to repair charges.')
        self.assertEqual(car.price, 15700.0)
        self.assertEqual(len(car.repairs), 1)

        result = car.need_repair(10000, "Replace engine")
        self.assertEqual(result, 'Repair is impossible!')
        self.assertEqual(car.price, 15700.0)
        self.assertEqual(len(car.repairs), 1)

    def test_comparison(self):
        self.assertEqual(self.car1 > self.car2, 'Cars cannot be compared. Type mismatch!')
        self.assertEqual(self.car2 > self.car1, 'Cars cannot be compared. Type mismatch!')

    def test_str_representation(self):
        expected_output = "Model Toyota | Type Sedan | Milage 20000km" \
                          "\nCurrent price: 15000.00 | Number of Repairs: 0"
        self.assertEqual(str(self.car1), expected_output)


if __name__ == '__main__':
    main()
