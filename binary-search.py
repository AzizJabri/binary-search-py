
def binary_search(arr,x):
    low = 0
    high = len(arr) - 1
    mid = 0

    while low <= high :
        mid = (low + high) // 2
        if arr[mid] < x :
            # ignoring left half
            low = mid + 1
        elif arr[mid] > x :
            # ignoring right half
            high = mid - 1
        else :
            # X is present at mid
            return mid
    # x is not present
    return -1
#enter sorted array here
arr = [-1,1,3,5,8,10,12,15,18,19,25,29,35,38,39,40,44,48,49]
# reading x
x = int(input('Enter X '))
# getting the index of x in sorted array
result = binary_search(arr,x)

if result != -1 :
    print('the item',x,'is present at the index ', str(result))
else:
    print('the item',x,' is not present')

