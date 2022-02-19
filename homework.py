# i = 0
# while i <= 10:
#     i = i + 1
#     if i > 7:
#         i = i + 2
# print(i)
# # 9 итераций цикла в проекте


# n = int(input())
# c = 1
# while c <= n:
#     print('*' * c)
#     c += 16

# n = 10
# width = n
# i = 1
# print(" " * n + "*")
# while i <= n:
#     print(' ' * (width - i) + '*' * i + '*' * i)
#     i += 1

# x = 10
# for i in range(x):
#     print(' ' * (x - i - 1), '*' * (i * 2 + 1))

# i = 0
# while i < 5:
#     print('*')
#     if i % 2 == 0:
#         print('**')
#     if i > 2:
#         print('***')
#     i = i + 1

# z = 0
# for i in range (10):
#     z = z + i
# print(z)

# s = 0
# while True:
#     x = int(input())
#     if x == 0:
#         print(s)
#         break // Оператор завершения цикла
#     s += x

# a = 2
# b = 5
# sum = 0
# while a <= b:
#     sum += a
#     a = a + 1
# print(sum)

# Алгоритм евклида - НОД(a,b) = НОД(a - b, b) ( при условии a > b )
# a, b = int(input()), int(input())
# c = max(a,b)
# while c % a != 0 or c % b != 0:
#     c += 1
# print(c)

# i = 0
# while i<5:
#     a, b =input().split() #если у тебя на вход подаются значения в одной строке то нужен split()
# если значения подаются в нескольких строках то .split() не нужен
#     a = int(a)
#     b = int(b)
#     if (a == 0) and (b == 0):
#         break # досрочное завершаем цикл
#     if (a == 0) or (b == 0):
#         continue # переходим к следующей итерации
#     print(a*b)
#     i += 1


# i = 0
# s = 0
# while i < 10:
#     i = i + 1
#     s = s + i
#     if s > 15:
#         break
#     i = i + 1
# print(i)


# i = 0
# while i <= 100:
#     x = int(input())
#     if x > 100:
#         break
#     if x < 10:
#         continue
#     print(x)

# n = int(input())
# for i in range(n):
#     print('*'*n)

# range(start = 0,to,step = 1) # stop =-1


# n = int(input())
# for i in range(n):
#
# a = 7
# b = 10
# c = 5
# d = 6
#
# for second_pare_number in range(c, d + 1):
#         # print(f'\t{second_pare_number}', end='')
#         print(f'\t{second_pare_number}', end='')
#
# print()  # чтобы был нормальный перенос
#
# for first_pare_number in range(a, b + 1):
#         print(f'{first_pare_number}\t', end='')
#         for second_pare_number in range(c, d + 1):
#                 print(f'{first_pare_number * second_pare_number}\t', end='')
#         print()


# a = range(int(input()), int(input()) + 1)
# b = range(int(input()), int(input()) + 1)
# print(" ", *b, sep="\t")
# for i in a:
#     print(i, *(i * j for j in b), sep="\t")

# a = range(int(input()), int(input()) + 1)
# b = range(int(input()), int(input()) + 1)
# print(" ", *b, sep="\t")
# for i in a:
# print(i, *(i * j for j in b), sep="\t")