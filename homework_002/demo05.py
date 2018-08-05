pizzas=['a pizza','b pizza','c pizza','d pizza','e pizza']
print('The first three items in the list are:')
for pizza in pizzas[0:3]:
	print('\t'+pizza)
print('Three items from the middle of the list are:')
for pizza in pizzas[1:4]:
	print('\t'+pizza)
print('The last three items in the list are:')
for pizza in pizzas[-3:]:
	print('\t'+pizza)
friend_pizzas=pizzas[:]
print('my pizzas:\n'+str(pizzas))
print('friend pizzas:\n'+str(friend_pizzas))
pizzas.append('add_f pizza')
friend_pizzas.append('f_add_g pizza')
print('my pizza add after:')
for my_pizza in pizzas:
	print('\t'+my_pizza)
print('friend pizza add after:')
for friend_pizza in friend_pizzas:
	print('\t'+friend_pizza)
