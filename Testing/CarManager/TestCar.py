from Testing.CarManager import car_manager
from unittest import TestCase, main


class TestCar(TestCase):

    def setUp(self):
        self.car = car_manager.Car("Nissan", "GT-R", 15, 75)

    def test_initializing(self):
        self.assertEqual("Nissan", self.car.make)
        self.assertEqual("GT-R", self.car.model)
        self.assertEqual(15, self.car.fuel_consumption)
        self.assertEqual(75, self.car.fuel_capacity)
        self.assertEqual(0, self.car.fuel_amount)

    def test_no_make_making(self):
        with self.assertRaises(Exception) as ex:
            car = car_manager.Car("", "GT-R", 15, 75)

        self.assertEqual("Make cannot be null or empty!", str(ex.exception))

    def test_no_model_error(self):
        with self.assertRaises(Exception) as ex:
            car = car_manager.Car("Nissan", "", 15, 75)

        self.assertEqual("Model cannot be null or empty!", str(ex.exception))

    def test_not_positive_fuel_consumption_error(self):
        with self.assertRaises(Exception) as ex:
            car = car_manager.Car("Nissan", "GT-R", 0, 75)

        self.assertEqual("Fuel consumption cannot be zero or negative!", str(ex.exception))

    def test_not_positive_fuel_capacity_error(self):
        with self.assertRaises(Exception) as ex:
            car = car_manager.Car("Nissan", "GT-R", 15, 0)

        self.assertEqual("Fuel capacity cannot be zero or negative!", str(ex.exception))

    def test_negative_fuel_amount_error(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_amount = -5

        self.assertEqual("Fuel amount cannot be negative!", str(ex.exception))

    def test_fuel_amount_change(self):
        expected = 5
        self.car.fuel_amount = expected
        self.assertEqual(expected, self.car.fuel_amount)

    def test_not_positive_refuel_error(self):
        with self.assertRaises(Exception) as ex:
            self.car.refuel(0)

        self.assertEqual("Fuel amount cannot be zero or negative!", str(ex.exception))

    def test_fuel_amount_adding(self):
        expected = 5
        self.car.refuel(expected)
        self.assertEqual(expected, self.car.fuel_amount)

    def test_over_refueling(self):
        expected = self.car.fuel_capacity
        self.car.refuel(1000)
        self.assertEqual(expected, self.car.fuel_capacity)

    def test_drive_not_enough_fuel_error(self):
        with self.assertRaises(Exception) as ex:
            self.car.drive(100)

        self.assertEqual("You don't have enough fuel to drive!", str(ex.exception))

    def test_fuel_change_after_driving(self):
        self.car.refuel(1000)
        self.car.drive(10)
        self.assertEqual(73.5, self.car.fuel_amount)


if __name__ == "__main__":
    main()