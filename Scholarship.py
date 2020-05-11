# Problem Link
# https://www.codechef.com/problems/ZCOSCH

rank = int(input())
value = 0
if 1 <= rank <= 50:
    value = 100
elif 51 <= rank <= 100:
    value = 50
else:
    value = 0
print(value)
