nums=[2,2,1]
dic={}
def single_num():
    for x in nums:
        if x not in dic:
            dic[x]=1
        else:
            dic[x]+=1
    for k,v in dic.items():
        if v==1:
            return k            
print(single_num())