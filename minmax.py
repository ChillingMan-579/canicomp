numbers = []

while True:
    num = input("enter number num/x : ")
    if num != "x":
        numbers.append(int(num))
    else:
        break

def max_check(nums):
    max_val = nums[0]
    for num in nums:
        if num > max_val:
            max_val = num
    return max_val

def min_check(nums):
    min_val = nums[0]
    for num in nums:
        if num < min_val:
            min_val = num
    return min_val

print("max = ", max_check(numbers))
print("min = ", min_check(numbers))