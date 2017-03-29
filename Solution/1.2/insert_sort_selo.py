from array import array
import random


def generate_test_data():
    size = random.randint(10, 50)
    data = list((range(size)))
    random.shuffle(data)
    return array('i', data)


def insert_sort(arr):
    for i, el in enumerate(arr):
        j = i - 1
        while j > -1 and arr[j] > el:
            arr[j+1] = arr[j]
            arr[j] = el #TODO: Optimazation needed. This code should operate one time per one loop.
            j -= 1
    return arr


def test_insert_sort():
    arr = generate_test_data()
    result = insert_sort(arr)
    if result.tolist() != sorted(arr):
        raise AssertionError("%s\n%s" % (result.tolist(), sorted(arr)))
    print("Success")


if __name__ == '__main__':
    test_insert_sort()
