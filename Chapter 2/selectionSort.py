# can sort in ascending order, descending order

def findSmallest(array):
  minElement = array[0]
  minIndex = 0
  for i in range(1, len(array)):
    if array[i] < minElement:
    # if array[i] > minElement:
      minElement = array[i]
      minIndex = i
  return minIndex


def ssort(array):
  returnArray = []
  
  for i in range(len(array)):
    minIndex = findSmallest(array)
    returnArray.append(array.pop(minIndex))
  
  return returnArray

inputArray = [4,3,2,1,10,8,9,7,5,6]
newArray = ssort(inputArray)
print(newArray)