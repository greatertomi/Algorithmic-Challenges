# Question link
# https://www.codechef.com/problems/RECNDNOS


def chefNumber(array):
    dishes = set(array)
    num_dict = {}
    for num in dishes:
        num_dict[num] = 0
        counter = 0
        while counter < len(array):
            if array[counter] == num:
                num_dict[num] += 1
                counter += 2
            else:
                counter += 1
    return max(num_dict, key=num_dict.get)


cases = int(input())
for _ in range(cases):
    input_number = input()
    numbers = input()
    arr = [int(x) for x in numbers.split()]
    print(chefNumber(arr))


# arr1 = [1, 2, 2, 1, 2, 1, 1, 1, 1]
# arr2 = [1, 1, 1, 1, 1, 1]
# arr3 = [2, 1, 1, 1, 2]
# arr4 = [1, 2, 2, 2, 3, 4, 2, 1]
# print(chefNumber(arr4))
