nums=[9,6,4,2,3,5,7,0,1]
sum=0
total=0
for x in range(len(nums)+1):
    total=total+x
for each in nums:
    sum=sum+each
miss_num=total-sum
print(miss_num)