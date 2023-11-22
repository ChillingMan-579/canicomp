def selection_sort(arr):
  for i in range (0, len(arr)):
    min = arr[len(arr)-1]
    min_index = len(arr)-1
    for j in range (i, len(arr)):
      if arr[j] < min:
        min = arr[j]
        min_index = j
    temp = arr[i]
    arr[i] = min
    arr[min_index] = temp
  print(arr)

def insertion_sort(arr):
  for i in range (1, len(arr)):
    key = arr[i]
    j = i-1
    while j >= 0 and key < arr[j]:
      arr[j+1] = arr[j]
      j -= 1
    arr[j+1] = key
  print(arr)

def merge_sort(arr):
  if len(arr) <= 1:
    return

  middle = len(arr)//2
  left = arr[:middle]
  right = arr[middle:]

  j = middle

  for k in range (0, len(arr)):
    if(k < middle):
      left[k] = arr[k]
    else:
      right[j - middle] = arr[k]
      j += 1

  merge_sort(left)
  merge_sort(right)
  merge(left, right, arr)
  print(arr)

def merge(left_arr, right_arr, arr):
  left_size = len(left_arr)
  right_size = len(right_arr)
  i, r, l = 0, 0, 0

  while l < left_size and r < right_size:
    if left_arr[l] < right_arr[r]:
      arr[i] = left_arr[l]
      l += 1
      i += 1
    else:
      arr[i] = right_arr[r]
      i += 1
      r += 1
  while l < left_size and i < len(arr):
    arr[i] = left_arr[l]
    i += 1
    l += 1
  while r < right_size and i < len(arr):
    arr[i] = right_arr[r]
    i += 1
    r += 1

selection_sort([11, 55, 77, 22, 1, 4])
insertion_sort([11, 55, 77, 22, 1, 4])
merge_sort([11, 55, 77, 22, 1, 4])