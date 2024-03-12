
# to multiply two matrix
mat1=[[1,5,4],[5,8,2],[8,6,2]]
mat2=[[4,6,1],[6,3,2],[9,8,2]]
result=[[0,0,0],[0,0,0],[0,0,0]]
for i in range(len(mat1)):
    for j in range(len(mat2)):
      result[i][j]=mat1[i][j]*mat2[i][j]

print(result)
