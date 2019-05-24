def spy_game(nums):
    c=0
    for n in nums:
        if n == 7 and nums[c-1] == 0 and nums[c-2] == 0:
            return True
        c+=1
    return False

print('Passing [1,2,3,4,5,6,7,8,9]')
print(spy_game([1,2,3,4,5,6,7,8,9]))
print("Passing [1,2,3,4,5,6,6,8,9]")
print(spy_game([1,2,3,4,5,6,6,8,9]))
print("Passing [1,2,3,4,5,0,7,8,9]")
print(spy_game([1,2,3,4,5,0,7,8,9]))
print("Passing [1,2,3,4,0,6,7,8,9]")
print(spy_game([1,2,3,4,0,6,7,8,9]))
print("Passing [1,2,3,4,0,0,7,8,9]")
print(spy_game([1,2,3,4,0,0,7,8,9]))
print("Passing [0,0,7,4,5,6,6,8,9]")
print(spy_game([0,0,7,4,5,6,6,8,9]))
print("Passing [1,2,3,4,5,6,0,0,7]")
print(spy_game([1,2,3,4,5,6,0,0,7]))
