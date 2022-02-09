
def my_range(start, end, step=1):
    arr = [start]
    while start + step < end:
        start += step
        arr.append(start)
    return arr
