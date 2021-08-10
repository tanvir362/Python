def merge(left, rignt):
    merged = []
    i, j = 0, 0
    size_left = len(left)
    size_right = len(rignt)

    while i<size_left and j<size_right:
        if left[i] < rignt[j]:
            merged.append(left[i])
            i = i+1
        else:
            merged.append(rignt[j])
            j = j+1
    
    merged = merged + (left[i:] if i<size_left else []) + (rignt[j:] if j<size_right else [])

    return merged

def merge_sort(arr):
    divider = int(len(arr)/2)

    if divider != 0:
        left = arr[:divider]
        right = arr[divider:]

        return merge(merge_sort(left), merge_sort(right))
    
    return arr







print(merge_sort([2, 8, 9, 7, 10, 1, 12, 5, 6]))