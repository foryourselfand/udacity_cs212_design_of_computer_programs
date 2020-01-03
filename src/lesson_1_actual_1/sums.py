from typing import List, Union


# def ss(nums):
#     total = 0
#     for i in range(len(nums)):
#         total = (total + nums[i] ** 2)
#     return total


# def ss(nums):
#     return sum(x ** 2 for x in nums)


# def sum_squares(numbers: List[Union[int, float]]) -> Union[int, float]:
#     total: Union[int, float] = 0
#     for index in range(len(numbers)):
#         total += numbers[index] ** 2
#     return total


def sum_squares(numbers: List[Union[int, float]]) -> Union[int, float]:
    return sum(number_element ** 2 for number_element in numbers)


def main():
    print(sum_squares([1, 2, 3, 4, 5]))


if __name__ == '__main__':
    main()
