from Testing.ListProject import extended_list
from unittest import TestCase, main


class TestIntegerList(TestCase):

    def setUp(self):
        self.integer_list = extended_list.IntegerList('50', 1, False, 3.5, 2, 3)

    def test_initializing(self):
        expected = [1, 2, 3]
        actual = self.integer_list.get_data()
        self.assertEqual(expected, actual)

    def test_add_operation_list_change(self):
        expected = self.integer_list.get_data() + [5]
        self.integer_list.add(5)
        self.assertEqual(expected, self.integer_list.get_data())

    def test_add_operation_error(self):
        with self.assertRaises(ValueError) as ex:
            self.integer_list.add(5.5)

        self.assertEqual("Element is not Integer", str(ex.exception))

    def test_remove_index_operation_return(self):
        expected = 2
        self.assertEqual(expected, self.integer_list.remove_index(1))

    def test_remove_index_operation_list_after_removing(self):
        expected = [1, 3]
        self.integer_list.remove_index(1)
        self.assertEqual(expected, self.integer_list.get_data())

    def test_remove_index_operation_error(self):
        with self.assertRaises(IndexError) as ex:
            self.integer_list.remove_index(100)

        self.assertEqual("Index is out of range", str(ex.exception))

    def test_get_return(self):
        expected = 2
        self.assertEqual(expected, self.integer_list.get(1))

    def test_get_index_error(self):
        with self.assertRaises(IndexError) as ex:
            self.integer_list.get(100)

        self.assertEqual("Index is out of range", str(ex.exception))

    def test_insert_valid_index_and_type_return(self):
        expected = [1, 2, 4, 3]
        self.integer_list.insert(len(self.integer_list.get_data()) - 1, 4)
        self.assertEqual(expected, self.integer_list.get_data())

    def test_insert_index_error(self):
        with self.assertRaises(IndexError) as ex:
            self.integer_list.insert(100, 100)

        self.assertEqual("Index is out of range", str(ex.exception))

    def test_insert_value_error(self):
        with self.assertRaises(ValueError) as ex:
            self.integer_list.insert(1, 5.5)

        self.assertEqual("Element is not Integer", str(ex.exception))

    def test_get_biggest(self):
        expected = 3
        self.assertEqual(expected, self.integer_list.get_biggest())

    def test_get_index(self):
        expected = 0
        self.assertEqual(expected, self.integer_list.get_index(1))


if __name__ == '__main__':
    main()