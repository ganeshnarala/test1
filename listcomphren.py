data="python is a opensorce language"
words=data.split()
x=[[w.upper(),w.lower(),len(w)] for w in words]
for p in x:
    print(p)