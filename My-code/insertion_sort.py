nums: list = [7, 2, 5, 3, 9]
#            [0, 1, 2, 3, 4]

# sorted = []

# for i in range(len(nums)):
    
#     print("list", nums)
#     value = nums[i]
#     index_value = i
#     print("index",index_value)
#     print("value",value)
#     print("sorted", nums[:i])
#     print("unsorted", nums[i:])
#     print("=" * 40)

#     for j in range(len(nums[:i])):
        
#         if value not in nums[:i]:
#             sorted_index = nums[:i].index(nums[j])
#             print(f"index sorted: {sorted_index}")
#             print(f"value sorted: {nums[j]}")
            
#             if value < nums[j]:
#                 print(f"{value} < {nums[j]}")
#                 value = nums.pop(index_value)
#                 nums.insert(sorted_index, value)
#                 print(nums)
#             else:
#                 print(f"{value} > {nums[j]}")
                
#             last = len(nums) -1
#             if max(nums[:i]) == nums[last]:
#                 print(f"it is sorted: {nums}")
#                 break 
        
#         print("-" * 40)
        

sorted = []

for i in range(len(nums)):
    
    print("list", nums)
    value = nums[i]
    index_value = i
    print("index",index_value)
    print("value",value)
    print("sorted", nums[:i])
    print("unsorted", nums[i:])
    print("=" * 40)

    for j in range(len(nums[:i])):
        
        
        print("-" * 40)
        

   

