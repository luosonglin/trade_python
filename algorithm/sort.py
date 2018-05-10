def quickSort(L, low, high):
    i = low
    j = high
    if i >= j:
        return L
    key = L[i]

    while i < j:
        while i < j and L[j] >= key:
            j -= 1
        L[i] = L[j]
        while i < j and L[i] <= key:
            i += 1
        L[j] = L[i]

    L[i] = key
    quickSort(L, low, i - 1)
    quickSort(L, j + 1, high)
    return L


A = [6, 2, 7, 3, 8, 5.1, 9]
quickSort(A, 0, len(A)-1)
print(A)
