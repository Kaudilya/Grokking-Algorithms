def binarySearch(item,target):
  low = 0
  high = len(item)-1
  
  while low <= high:
    mid = (low+high) // 2
    print("At index",mid)
    guess = item[mid]

    if guess == target:
      return mid
    elif guess < target:
      low = mid+1
    elif guess > target:
      high = mid-1
  return 0


myArray = [1,2,3,4,5,6,7,8,9,10]
resultIndex = binarySearch(myArray,3)
print(resultIndex)