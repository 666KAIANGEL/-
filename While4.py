import random

N = 81
print('N = ', N)

while N >= 3:
    N /= 3
print("Является степенью 3: ", (N==1))