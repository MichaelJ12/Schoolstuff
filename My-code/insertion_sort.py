nums: list = [7, 2, 5, 3, 9]
#            [0, 1, 2, 3, 4]

sorted = []

for i in range(len(nums)):
    print("sorted", sorted)
    print("list", nums[i:])
    value = nums[i]
    print("value",value)
    index_value = i + nums[i:].index(value)
    print("index",index_value)
    sorted.append(value)

    
    print("-" * 40)
   

