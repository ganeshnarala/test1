x=[[10,'book',500.00],[40,'mobile',7500.00],[70,'bike',6597.00]]
print(x)
for p in x:
 print(p)
 x.sort(reverse=True)
for q in x:
 print(q)
 x.sort(key=lambda c:c[2],reverse=True)
 for r in x:
  print(r)