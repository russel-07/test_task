# В данной функции, для реализации сортировки использован алгоритм сортировки
# слиянием. Сложность данного алгоритма сосотавлет O(n log n).
# Алгоритм сортировки, основанный на сравнении элементов между собой
# невозможно созадть со сложностью менее чем O(n log n), что доказывается
# математически.
# Есть алгоритмы сортировки, основанные на других принципах и могут работать
# быстрее, например поразрядная сортировка, сортировка подсчетом,
# но в данной задаче, при определенных входных данных, такие алгоритмы
# будут работать медленнее, а сортировка слиянием всегда будет работать за
# O(n log n).

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


def check_sort_func():
    arr_1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    arr_2 = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
    arr_3 = [17, 135, 4, 28, 69, 13024, 1989]
    assert mergesort(arr_1) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    assert mergesort(arr_2) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    assert mergesort(arr_3) == [4, 17, 28, 69, 135, 1989, 13024]
    print('Sorting function works correctly!')
