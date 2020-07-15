from nearest_greatest_smallest import nearest_greatest_to_left, nearest_greatest_to_right, nearest_smallest_to_left, nearest_smallest_to_right

def maximum_area_in_histogram(arr):
    nsr_tuple, nsl_tuple = nearest_smallest_to_right(arr), nearest_smallest_to_left(arr)
    
    print(nsr_tuple)
    print(nsl_tuple)
    maximum_area_histogram = []
    for idx, value in enumerate(arr):

        nsr_index = nsr_tuple[idx][2]
        nsl_index = nsl_tuple[idx][2]
        maximum_area_histogram.append(arr[idx] * (nsr_index - nsl_index - 1))
    print(maximum_area_histogram)

print(maximum_area_in_histogram([6,2,5,4,5,1,6]))