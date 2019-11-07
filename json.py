import json
data={}
data['people']=[]
data['people'].append({'name':'scott','website':'facebook.com','from':'nebraska'})
data['people'].append({'name':'larry','website':'google.com','from':'machigan'})
data['people'].append({'name':'tira','website':'apple.com','from':'albama'})
fil = open('data.json','w')
json.dump(data,fil)
fil.close()
