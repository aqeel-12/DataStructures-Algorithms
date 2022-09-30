nums = [1,1]
def dis_num():
    dic_nums=set(nums)
    res=[]
    for x in range(1,len(nums)+1):
        if x not in dic_nums:
            res.append(x)
    return res
print(dis_num())            