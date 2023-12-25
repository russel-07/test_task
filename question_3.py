def mergesort(arr):
    if len(arr) <= 1:
        return arr
    if len(arr) == 2:
        if arr[0] > arr[1]:
            arr[0], arr[1] = arr[1], arr[0]
        return arr
    
    mid = len(arr) // 2
    left_arr = mergesort(arr[:mid])
    right_arr = mergesort(arr[mid:])

    return merge(left_arr, right_arr)


def merge(arr_1, arr_2):
    arr = []
    if len(arr_1) == 0:
        arr = arr_2
    elif len(arr_2) == 0:
        arr = arr_1
    else:
        i, j = 0, 0
        while 1:
            if arr_1[i] < arr_2[j]:
                arr.append(arr_1[i])
                if i == (len(arr_1) - 1):
                    arr += arr_2[j:]
                    break
                else:
                    i += 1
            else:
                arr.append(arr_2[j])
                if j == (len(arr_2) - 1):
                    arr += arr_1[i:]
                    break
                else:
                    j += 1
    return arr
