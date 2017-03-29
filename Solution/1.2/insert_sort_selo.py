from array import array
import random


def generate_random_array():
    size = random.randint(10, 50)
    data = list((range(size)))
    random.shuffle(data)
    return array('i', data)


def insertion_sort(arr):
    for i, el in enumerate(arr):
        while i > 0 and arr[i-1] > el:
            arr[i] = arr[i-1]
            i -= 1
        arr[i] = el #TODO: Optimazation needed. This code should operate one time per one loop.
    return arr


def test_insert_sort():
    arr = generate_random_array()
    result = insertion_sort(arr)
    if result.tolist() != sorted(arr):
        raise AssertionError("%s\n%s" % (result.tolist(), sorted(arr)))
    print("Success")


if __name__ == '__main__':
    test_insert_sort()
