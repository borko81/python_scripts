import unittest

class Deque:
    def __init__(self):
        self.deq = []

    def enque(self, number):
        self.deq.append(number)
    
    def __get_element(self):
        return self.deq[0]

    def peek(self):
        return self.__get_element()

    def deque(self):
        try:
            temp = self.__get_element()
            del self.deq[0]
        except IndexError as ex:
            raise ex
        else:
            return temp

    @property
    def len(self):
        return len(self.deq)


class TestDeque(unittest.TestCase):
    def setUp(self):
        self.d = Deque()

    def test_corect_set_param(self):
        """
        Test all param is set corect
        """
        print(self.shortDescription())
        self.assertEqual(self.d.deq, [])

    def test_enque_add_element_to_list(self):
        self.d.enque(1)
        self.assertListEqual(self.d.deq, [1])

    def test_deque_remove_element_from_list(self):
        self.d.enque(1)
        self.d.enque(2)
        self.d.deque()
        self.assertListEqual(self.d.deq, [2])

    def test_deque_remove_element_from_empty_list_should_raise_error(self):
        with self.assertRaises(IndexError) as er:
            self.d.deque()

    def test_len_deq_with_empy_size(self):
        self.assertEqual(self.d.len, 0)
        


if __name__ == '__main__':
    unittest.main(verbosity=2)

    # d.enque(1)
    # print(d.deq)
    # d.enque(2)
    # print(d.deq)
    # d.deque()
    # print(d.deq)