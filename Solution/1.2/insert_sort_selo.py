from array import array
import random


def generate_test_data():
    size = random.randint(10, 50)
    data = list((range(size)))
    random.shuffle(data)
    return array('i', data)


def insert_sort(arr):
    n = len(arr)
    for i, el in enumerate(arr):
        key = el
        j = i - 1
        while j > -1 and arr[j] > key:
            arr[j+1] = arr[j]
            arr[j] = key
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
