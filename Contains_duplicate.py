nums = [1,2,3,4]

def contain_dup():
    dic={}
    for each in nums:
        if each in dic:
            return True
        else:
            dic[each]=1
    return False

print(contain_dup())


