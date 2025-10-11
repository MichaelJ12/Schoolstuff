my_list: list = [2, 3, 1, 1, 4]

current: int = 1
jumps: int = 0

 # next jump needs to be the optimal jump in this case + 1 to go to index 1 not 2 to reach the end in 2 jumps
jump_range = range(1, my_list[current] + 1) 


for r in jump_range:
    next_jump = r
    print("=" * 40) 
    print(r)
    print("-" * 40) 
    print(f"i jumped: {next_jump} steps")
    print("=" * 40) 




next_jump = current + my_list[current]

if 0 <= current < len(my_list):
    print("yes")
else:
    print("nope")