#-*- coding: utf-8 -*-

from array import array
import random
import inspect


def generate_random_bit_array(length=5):
    sample = (0, 1)
    data = [random.choice(sample) for v in range(length)]
    return array('b', data)


def sum_bit_array(a, b):
    pass


def extract_arguments_from_func(func):
    sig = inspect.signature(func)
    parameters = sig.parameters
    return dict(parameters)


def test_sum_bit_array():
    print('start testing...')
    arr1 = generate_random_bit_array()
    arr2 = generate_random_bit_array()
    print(arr1, arr2)
    result_arr = sum_bit_array(arr1, arr2)

    # practice code
    arguments_dict = extract_arguments_from_func(generate_random_bit_array)
    try:
        length_param = arguments_dict['length']
        test_arr_length = length_param.default
    except KeyErrr as e:
        raise AssertionError(e)

    assert test_arr_length + 1 == len(result_arr)
    # TODO: bit 를 요소로 갖는 길이가 같은두 배열이 있다. 
    # 이 두 배열의 각각의 요소를 더해 새로운 배열을 만들때,
    # 두 배열의 합으로 만들어진 배열이 정상적으로 만들어 졌는지 어떻게 검증할 수 있을까?


def main():
    test_sum_bit_array()


if __name__ == "__main__":
    main()
