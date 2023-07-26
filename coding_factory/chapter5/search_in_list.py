# Search with: in, index(), count()

nums = [1, 2, 3, 4, 5]

nums_to_find = 20

# in operator    
if nums_to_find in nums:
    print("found it")

else:
    print("not found") # not found

# method index()
try:
    index = nums.index(nums_to_find)
    print("found")
except ValueError as e:
    print("Value error:", e)   #Value error: 20 is not in list

# method count()
count = nums.count(nums_to_find)

if count > 0:
    print(f"{nums_to_find} is present {count} times in th list")
else:
    print(f"{nums_to_find} is not present in the list")  #20 is not present in the list