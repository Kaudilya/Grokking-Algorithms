def quickSort(arr):
  if len(arr) < 2:
    return arr
  # else:
  pivot = arr[0]
  less = [i for i in arr[1:] if i<pivot]
  more = [j for j in arr[1:] if j>pivot]

  return quickSort(less) + [pivot] + quickSort(more)


numbers=[1,5,2,44,12,9]
print(quickSort(numbers))

print([0]+[2])
print([]+[2])