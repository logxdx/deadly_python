def pascal_triangle_row(n):
    if n == 0:
        return [1]
    elif n == 1:
        return [1, 1]
    else:
        prev_row = pascal_triangle_row(n - 1)
        row = [1] + add_adjacent(prev_row) + [1]
        return row

def add_adjacent(row):
    if len(row) == 1:
        return []
    else:
        return [row[0] + row[1]] + add_adjacent(row[1:])

for i in range(int(input())):
    print(pascal_triangle_row(i))
