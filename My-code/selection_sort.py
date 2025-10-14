nums: list = [7, 2, 5, 3, 9]
#            [0, 1, 2, 3, 4]
def selection_sort(nums) -> None:
    sorted = []


    for i in range(len(nums) - 1):
        print(i)
        current_min = min(nums)
        current_index = nums.index(current_min)
        
        nums.pop(current_index)
        sorted.append(current_min)
        print(current_min)
        print(nums)
        print(sorted)
        print("_" * 40)
    
    if nums:
        last = max(nums)
        print(last)
        # last = nums.index(last)
        sorted.append(last)
        nums.pop(0)
       
        print("we got the last number")
        print(nums)
        print(sorted)
        print("=" * 40)
        
def selection_sort_classic(nums) -> None:
       

    for i in range(len(nums) - 1):
        print(nums) 
        print("index:", nums[i])
        current_min = min(nums[i:len(nums)])
        current_index = nums.index(current_min)
        j = nums[i:].index(min(nums))
        print(f"min: {current_min} index: {current_index}")
        j, current_index = current_index, j
        print(f"{j, current_index} = {current_index, j}")
        print(nums)
        print("-" * 40)
    








if __name__ ==  "__main__":
    # print(selection_sort(nums))
    print(selection_sort_classic(nums))
