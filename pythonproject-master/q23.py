# wap to transpose a matrix

x=[[3,5,1],
   [5,8,2],
   [7,9,2]]
y=[[0,0,0],[0,0,0],[0,0,0]]
for i in range(len(x)):
    for j in range(len(x[0])):
      y[j][i]=x[i][j]
print(y)