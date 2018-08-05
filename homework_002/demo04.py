for value in range(1,21):
	print(value)
nums=list(range(1,1000001))
#print(nums)
print('min:'+str(min(nums)))
print('max:'+str(max(nums)))
print('sum:'+str(sum(nums)))
jishus=list(range(1,21,2))
for jishu in jishus:
	print(jishu)
chu3s=list(range(3,30,3))
for chu3 in chu3s:
	print(chu3)
lifangs=[]
for i in range(1,11):
	lifangs.append(i**3)
for lifang in lifangs:
	print(lifang)
squars=[value**3 for value in range(1,11)]
for squar in squars:
	print(squar)
