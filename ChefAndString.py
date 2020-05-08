# Question Link
# https://www.codechef.com/problems/RECNDSTR


def left(string):
    newString = ''
    for i in range(1, len(string)):
        newString += string[i]
    newString += string[0]
    return newString


def right(string):
    newString = string[len(string) - 1]
    for i in range(0, len(string) - 1):
        newString += string[i]
    return newString


value = int(input())
input_values = []
for _ in range(value):
    input_values.append(input())

for word in input_values:
    if left(word) == right(word):
        print('YES')
    else:
        print('NO')

# value = 'abcde'
#
# print(left(value))
# print(right(value))
