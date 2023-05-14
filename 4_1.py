# Заполнить список степенями числа 2 (от 2^1 до 2^n)


# N=int(input())
# A=[2**i for i in range(1,N+1)]
# print(A)
#
a = []

N = int(input()) #пользователь сам вводит сколько чисел ему нужно

for i in range(N):

   a.append(2**i)

print(a)



number = [1, 2, 3, 4, 5, 6, 7, 8, 9]
number = [number [i]*5 for i in range(len(number))]
print(number)

test = float ( "inf" )