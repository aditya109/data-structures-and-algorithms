def findPivot(arr):
    left, right = 0, len(arr) - 1
    n = len(arr)
    while left <= right:
        mid = left + (right - left) // 2
        next = (mid + 1) % n
        prev = (mid + n - 1) % n
        print(arr[mid], arr[prev], arr[next])
        if arr[mid] <= arr[next] and arr[mid] <= arr[prev]:
            return mid
        elif arr[mid] < arr[right]:
            right = mid - 1
        else:
            left = mid + 1


if __name__ == '__main__':
    arr = [5, 6, 7, 8, 9, 10, 1, 2, 3]
    key = 3
    print(findPivot(arr))
