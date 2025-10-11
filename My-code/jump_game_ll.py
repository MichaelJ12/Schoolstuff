nums: list = [2, 3, 1, 1, 4]
#       index[0, 1, 2, 3, 4] = 5

# You start at index 0. 
# The minimum jumps to reach the last index is 2 (0 -> 1 -> 4)

def jump_game(nums) -> int:
    explore_jump: list = [0]
    jumps: int = 0

    while explore_jump:
        current = explore_jump.pop()
        

        if current == len(nums) -1:
            print("we made the end")
            print("=" * 40)
            return jumps
        else:
            jump_range = range(1, nums[current] + 1) 
            for r in jump_range:
                next_jump = r
            
            # next jump needs to be the optimal jump in this case + 1 to go to index 1 not 2 to reach the end in 2 jumps
            print(f" the range of jumps it can make is: {range(nums[current])}")
            # next_jump = current + nums[current]
            if 0 <= current < len(nums):
                print(f"start: {current}")
                print("-" * 40)

                explore_jump.append(current)
                jumps += 1
                print(f"explore: {explore_jump}")
                print(f"next: {current}")
                print(f"jumps made: {jumps}")
                print("=" * 40)

    print("you cant make the end")
    print("=" * 40)

    return jumps 

jumps = jump_game(nums)

print(f"final number of jumps: {jumps}")

