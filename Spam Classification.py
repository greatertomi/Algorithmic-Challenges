# Question Link
# https://www.codechef.com/problems/SPAMCLAS

neural_net_num = 2
minX = 1
maxX = 4

even = 0
odd = 0
for n in range(neural_net_num):
    wi, bi = map(int, input().split())
    result_arr = []
    for i in range(minX, maxX+1):
        x = wi*i + bi
        result_arr.append(i)
        print(x)
print(even, odd)
