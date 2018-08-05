"""welcome to here"""
def make_shirt(t_char):
    print('This t-shart have '+t_char)

make_shirt('GOOD')
make_shirt(t_char='HAHA')

def make_shirt01(t_char='I love Python.'):
    print('Shirt is '+t_char)

make_shirt01()
make_shirt01('BIG')
make_shirt01('LITTLE')

def describe_city(city_name='Iceland',country='Reykjavik'):
    print(city_name+'\t'+country)
    
describe_city()
