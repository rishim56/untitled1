def rev(arr):
    len1=len(arr)
    for i in reversed(range(0,len1-1)):
        print(arr[i])


if __name__ == "__main__" :
    arr=[7,4,3,5,6,3]
    rev(arr)