# ~ sandwich_orders=['a_sandwich','b_sandwich','c_sandwich']
# ~ finished_sandwiches=[]
# ~ while sandwich_orders:
    # ~ one_sandwich=sandwich_orders.pop()
    # ~ print('I made your '+one_sandwich)
    # ~ finished_sandwiches.append(one_sandwich.upper())

# ~ print('Ok!')
# ~ for sandwich in finished_sandwiches:
    # ~ print('\t'+sandwich)
    
# ~ sandwich_orders=['pastrami','a_sandwich','b_sandwich','pastrami','c_sandwich','pastrami']
# ~ print(str(sandwich_orders))
# ~ print('The pastrami is over.')
# ~ while 'pastrami' in sandwich_orders:
    # ~ sandwich_orders.remove('pastrami')
# ~ print('Remove ok!')
# ~ for sw in sandwich_orders:
    # ~ print(sw)


while True:
    please=input('If you could visit one please in the world,where would you go?')
    print(please)
    again=input('Please again,entry YES/NO')
    if again.lower() == 'no':
        print('good by')
        break
