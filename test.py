fruits = ['banana', 'apple', 'pear', 'kiwi', 'pineapple', 'mango']

sorted_fruits = sorted(fruits, key=lambda w: len(w))

print(sorted_fruits)

short_f = filter(lambda w: len(w) <=4, fruits)

print(list(short_f))
#test

nums = [1,2,3,4,5]

new_nums = map(lambda w: w * w if w % 2 != 0 else w, nums)

print(list(new_nums)) 