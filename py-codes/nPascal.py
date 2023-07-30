def pascal_triangle_row(n):
    if n == 0:
        return [1]
    else:
        prev_row = pascal_triangle_row(n - 1)
        row = [1]
        for i in range(len(prev_row) - 1):
            row.append(prev_row[i] + prev_row[i + 1])
        row.append(1)
        return row
