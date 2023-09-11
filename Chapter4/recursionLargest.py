def largest(arr):
  if len(arr) == 2:
    if arr[0]>arr[1]:
      return arr[0]
    else:
      return arr[1]
  sub_max = largest(arr[1:])
  if arr[0] > sub_max:
    return arr[0]
  else:
    return sub_max
  
  # optimised of below is above.
  # elif arr[0] > largest(arr[1:]):
  #   return arr[0]
  # else:
  #   return largest(arr[1:])


numbers=[111,33,2,5,6]
result = largest(numbers)
print(result)

