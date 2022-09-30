original = [1,2,3]
m ,n = 1,4
# matrix=[]
# for x in range(m):
#     mat=[]
#     for y in range(n):  
#         mat.append(original[y:n-1])
#     matrix.append(mat)        
    
# print(matrix)
res=[]
for x in range(0, len(original), n):
    if m*n!=len(original): 
        print([])
    else: 
        res.append(original[x:x+n])
print(res)   
#-print(original[0:0+3])