nums = [3,1,3,4,2]
hare,tortoise=0,0
while True:
    hare=nums[hare]
    tortoise=nums[nums[tortoise]]
    if hare==tortoise:
        break
while True:
    hare2=0
    hare2=nums[hare2]
    tortoise=nums[tortoise]
    if hare2==tortoise:
        break
print(hare2)
