class FlatIterator:
    def __init__(self, list_of_lists):
        self.index = 0
        self.flat_list = [y for x in list_of_lists for y in x][::-1]
        self.total = len(self.flat_list)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= self.total:
            raise StopIteration
        self.index += 1

        return self.flat_list.pop()


def test_1():
    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):

        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]


if __name__ == '__main__':
    test_1()


