def merge(left, right):
    merged = []
    i, j = 0,0
    size_left = len(left)
    size_right = len(right)

    while i<size_left and j<size_right:
        if left[i] < right[j]:
            merged.append(left[i])
            i = i+1
        else:
            merged.append(right[j])
            j = j+1
    
    merged = merged + (left[i:] if i<size_left else []) + (right[j:] if j < size_right else [])
    
    return merged

def merge_sort(arr):
    divider = int(len(arr)/2)
    
    if divider != 0 :
        left = arr[:divider]
        right = arr[divider:]
        
        return merge(merge_sort(left), merge_sort(right))
    
    return arr


if __name__ == '__main__':
    # arr = [1,3,5,7]
    # arr2 = [4,6,8]
    print(merge_sort([5, 3, 7, 2, 4, 1, 9]))
    
    