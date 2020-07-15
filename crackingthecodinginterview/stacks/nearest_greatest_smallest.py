import random
def nearest_greatest_to_left(arr):
    l = len(arr)
    ngl_tuple = [] 
    # ngl_tuple contains (current_number, ngl, index of ngl)

    stack = []

    for i, v in enumerate(arr):
        if len(stack) == 0:
            stack.append((v, i))
            ngl_tuple.append((v, -1, -1))
        else:
            ngl_tuple.append((v, stack[-1][0], stack[-1][1]))
            current_max = stack.pop()
            if v > current_max[0]:
                stack.append((v, i))
            else: 
                stack.append(current_max)
    return ngl_tuple

def nearest_smallest_to_left(arr):
    l = len(arr)
    nsl_tuple = [] 
    # ngl_tuple contains (current_number, nsl, index of nsl)

    stack = []

    for i, v in enumerate(arr):
        if len(stack) == 0:
            stack.append((v, i))
            nsl_tuple.append((v, -1, -1))
        else:
            nsl_tuple.append((v, stack[-1][0], stack[-1][1]))
            current_min = stack.pop()
            if v < current_min[0]:
                stack.append((v, i))
            else: 
                stack.append(current_min)
    return nsl_tuple

def nearest_smallest_to_right(arr):
    l = len(arr)
    nsr_tuple = [] 
    # nsr_tuple contains (current_number, nsr, index of nsr)

    stack = []

    for i, v in enumerate(reversed(arr)):
        if len(stack) == 0:
            stack.append((v, l-i-1))
            nsr_tuple.insert(0, (v, -1, -1))
        else:
            nsr_tuple.insert(0, (v, stack[-1][0], stack[-1][1]))
            current_min = stack.pop()
            if v < current_min[0]:
                stack.append((v, l-i-1))
            else: 
                stack.append(current_min)
    return nsr_tuple

def nearest_greatest_to_right(arr):
    l = len(arr)
    ngr_tuple = [] 
    # ngr_tuple contains (current_number, ngr, index of ngr)

    stack = []

    for i, v in enumerate(reversed(arr)):
        if len(stack) == 0:
            stack.append((v, l-i-1))
            ngr_tuple.insert(0, (v, -1, -1))
        else:
            ngr_tuple.insert(0, (v, stack[-1][0], stack[-1][1]))
            current_max = stack.pop()
            if v > current_max[0]:
                stack.append((v, l-i-1))
            else: 
                stack.append(current_max)
    return ngr_tuple

# if __name__ == "__main__":
#     # arr = [27, 12, 43, 100, 18, 20, 23, 59, 60, 79]
#     arr = [random.randint(1, 100) for i in range(10)]

#     print(arr)
#     print(nearest_greatest_to_left(arr))
#     print(nearest_greatest_to_right(arr))
#     print(nearest_smallest_to_left(arr))
#     print(nearest_smallest_to_right(arr))