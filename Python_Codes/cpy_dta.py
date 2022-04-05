def cpy(arr):
    n=len(arr)
    arr1=[None]*n
    for i in range(0,len(arr)):
        arr1[i]=arr[i]

    print(arr1)

if __name__ == "__main__":
    arr=[2,3,4,5,6,7]
    cpy(arr)