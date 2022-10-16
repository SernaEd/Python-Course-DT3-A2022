def sum_range(end):
    if end > 0:
        return end + sum_range(end - 1)
    else:
        return 0
