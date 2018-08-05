
# ~ try:
    # ~ num01=input('Please entry first number:')
    # ~ int_num01=int(num01)
    # ~ num02=input('Please entry second number:')
    # ~ int_num02=int(num02)
    # ~ sum=int_num01+int_num02
    # ~ print('sum:'+str(sum))
# ~ except ValueError:
    # ~ print('Please input number.')

while True:
    try:
        num01=input('Please entry first number:')
        int_num01=int(num01)
        break
    except ValueError:
        pass
    
while True:
    try:
        num02=input('Please entry first number:')
        int_num02=int(num02)
        break
    except ValueError:
        pass
print('sum:'+str(int_num01+int_num02))
