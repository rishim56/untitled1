def sort(arr):
    len1 = len(arr)
    for i in range(0,len1-1):
        for j in range(0,len1-1):
            if arr[j]>arr[j+1]:
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
    print(arr)


if __name__ == "__main__" :
    arr = [3,9,2,7,6,5]
    sort(arr)
