nums = [1,2,3,4]
prefix=[]
postfix=[]
output=[]
pre=1
pos=1

for x in range(len(nums)):
    pre=pre*nums[x]
    prefix.append(pre)

for x in range(1,(len(nums)+1)):
    pos=pos*nums[-x]
    postfix.insert(-x,pos)

prefix.insert(0,1)
postfix.insert(len(postfix)+1,1)

for x in range(len(nums)):
    output.append(prefix[x]*postfix[x+1])
print(output)

