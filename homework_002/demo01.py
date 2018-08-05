friends=['shuZong','maJie','mengLaoshi']
print(friends)
print(friends[0]+' ,how are you.')
no_comming=friends.pop(0)
print(no_comming+' ,no comming.')
print(friends)
friends.insert(0,'zhaiZong')
print(friends)
print('I have find a lage table.')
friends.insert(0,'wang si yu.')
print(friends)
friends.insert(3,'zhangZhiPeng')
print(friends)
friends.append('xidada')
print(friends)
for name in friends:
	print('Welcome '+name.title())
print('I only welcome two friends.')
while len(friends)!=2:
	print("We next time see "+friends.pop())
print(friends)
for name in friends:
	print('Welcome to here '+name.upper())
del friends[0]
print(friends)
del friends[1]
print(friends)
