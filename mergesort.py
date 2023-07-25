#MERGE SORT

def mergeSort(arr):
    if len(arr) > 1:
        middle = len(arr)/2


        larr = arr[:middle]
        rarr = arr[middle:]

        mergeSort(larr)
        mergeSort(rarr)

        i = j = k = 0

        while i < len(larr) and j < len(rarr):
            if larr[i] <= rarr[j]:
                arr[k] = larr[i]
                i += 1
            else:
                arr[k] = rarr[j]
                j += 1
            k += 1
                
        while i < len(larr):
            arr[k] = larr[i]
            i += 1
            k += 1
        while j < len(rarr):
            arr[k] = rarr[j]
            j += 1
            k += 1
