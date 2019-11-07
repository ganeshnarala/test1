x=(10,20,30)
print(x)
print(type(x))
p=(100,200,300,400)
print(p)
q=(100,'ganesh',3+2j,45.96,True)
print(q)
print(q[2])
print(q[2:5])
print(q[-3])
print(q[-4:-2])

#..................#
x=(10,20,30,40,50,60,20)
print(20 in x)
print(75 in x)
for p in x:
    print(p)
i=0
while i<len(x):
    print(x[i])
    i+=1
print(x.count(20))
print(x.index(40))
print(x.index(20,3))

#..................#

x=((10,20,30),[45,True,2+5j],(40,50,60))
print(x)
for p in x:
    for q in p:
        print(q,end=" ")

    print()
x[1][1]=99
for a,b,c in x:
    print(a,b,c)

#....................#
x={10,20,30,40,50,60}
print(x)
print(type(x))
print(len(x))
y=set()
print(y)
z={100,200,300,200,100}
print(z)
p={"ganesh",True,False,100,25.96,2+6j,'2'}
for q in p:
    print(q)
p.add(70)
print(p)
print(p.remove(70))
print(p)
p.remove(True)
print(p)
p.discard(False)
print(p)
p.pop()
print(p)
p.clear()
print(p)

#..................#

x={(10,20,30),(40,50,60),(70,80,90)}
for p in x:
    for q in p:
        print(q,end=" ")
    print()
for a,b,c in x:
    print(a,b,c)

