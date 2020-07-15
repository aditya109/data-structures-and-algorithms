def stock_span_problem(arr, day):
    span_stack = []
    count = 0
    for i in range(day-1, -1, -1):
        if arr[i]<= arr[day-1]:
            span_stack.append(arr[i])
        else:
            count = max(count, len(span_stack))
            span_stack = []
    return count


if __name__ == "__main__":
    arr = [100, 80, 60, 70, 60, 75, 85]
    day = 6
    print(stock_span_problem(arr, day))