nums = list(map(lambda x: x ** 2, range(10)))
print(nums)

even1 = [x for x in range(10) if x % 2 == 0]
print(even1)

even2 = list(filter(lambda x: x % 2 == 0, range(10)))
print(even2)


# matrix

# list
matrix1 = [[x, y] for x in range(3) for y in range(3) if x % 2 == 0 and y % 2 == 0]
print(matrix1)

# tuple
matrix2 = [(x, y) for x in range(3) for y in range(3) if x % 2 == 0 and y % 2 == 0]
print(matrix2)

# set
matrix3 = [{x, y} for x in range(3) for y in range(3) if x % 2 == 0 and y % 2 == 0]
print(matrix3)
