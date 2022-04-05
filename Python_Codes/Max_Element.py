def maxElement(arr):
    n=len(arr)
    Max=arr[0]
    for i in range(0,n):
        if arr[i]>Max:
            Max=arr[i]

    print(Max)

if __name__ == "__main__":
    arr=[6,2,3,4,1,9,4,3,5,2]
    maxElement(arr)
