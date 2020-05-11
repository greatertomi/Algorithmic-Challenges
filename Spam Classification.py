# Question Link
# https://www.codechef.com/problems/SPAMCLAS
# My Solution, but could not handle large cases

cases = int(input())
for _ in range(cases):
    neural_net_num, minX, maxX = map(int, input().split())
    even = 0
    odd = 0
    num_array = []

    for i in range(minX, maxX + 1):
        num_array.append(i)

    for i in range(neural_net_num):
        w, b = map(int, input().split())
        for k in range(len(num_array)):
            num = (w * num_array[k]) + b
            if i == neural_net_num-1:
                if num % 2 == 0:
                    even += 1
                else:
                    odd += 1
            else:
                num_array[k] = num
    print(even, odd)

