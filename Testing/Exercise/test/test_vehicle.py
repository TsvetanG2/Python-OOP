from unittest import TestCase, main
from sys import maxsize
from project.vehicle import Vehicle

class TestsVehicle(TestCase):

    def setUp(self):
        self.vehicle = Vehicle(20.5, 300)

    def test_initializing(self):
        self.assertEqual(20.5, self.vehicle.fuel)
        self.assertEqual(20.5, self.vehicle.capacity)
        self.assertEqual(300, self.vehicle.horse_power)
        self.assertEqual(self.vehicle.DEFAULT_FUEL_CONSUMPTION, self.vehicle.fuel_consumption)

    def test_default_consumption(self):
        self.assertEqual(1.25, self.vehicle.DEFAULT_FUEL_CONSUMPTION)

    def test_not_enough_fuel_error(self):
        with self.assertRaises(Exception) as ex:
            self.vehicle.drive(maxsize)

        self.assertEqual("Not enough fuel", str(ex.exception))

    def test_vehicle_fuel_after_driving(self):
        expected = 19.25
        self.vehicle.drive(1)
        self.assertEqual(expected, self.vehicle.fuel)

    def test_vehicle_capacity_of_fuel_is_max(self):
        with self.assertRaises(Exception) as ex:
            self.vehicle.refuel(maxsize)

        self.assertEqual("Too much fuel", str(ex.exception))

    def test_vehicle_fuel_after_refuel(self):
        self.vehicle.drive(1)
        self.vehicle.refuel(1)
        expected = 20.25
        self.assertEqual(expected, self.vehicle.fuel)

    def test_string_representation(self):
        expected = f"The vehicle has {self.vehicle.horse_power} " \
                   f"horse power with {self.vehicle.fuel} fuel left and {self.vehicle.fuel_consumption} fuel consumption"

        self.assertEqual(expected, str(self.vehicle))

if __name__ == '__main__':
    main()




