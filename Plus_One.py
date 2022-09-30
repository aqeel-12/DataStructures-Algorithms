digits = [4,3,2,9]
result=[]
s=[str(i) for i in digits]
res=''.join(s)
res=int(res)+1
res=str(res)
for x in res:
    result.append(x)

print(result)    
