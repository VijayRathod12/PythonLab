lst=[5,7,12,34,1,2,5,7]
res=[]
for i in lst:
    if i  not in res:
      res.append(i)
print(res)