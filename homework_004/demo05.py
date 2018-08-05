def city_country(country,city):
    print(country.title()+','+city.title())

city_country('Santiago','Chile')

def make_album(singler,book,single_num=''):
    singler_des={'singler':singler,'book':book}
    if single_num:
        singler_des['single_num']=single_num
    return singler_des

singler_des=make_album('zhoujilun','qidukongjian')
print(singler_des)
singler_des=make_album('zhoujielun','qidukongjian',10)
print(singler_des)

while True:
    """This is loop"""
    print('\nPlease tell me you point.And you and input "q" everytime to quit.')
    country=input('Entry you country:')
    if country.lower()=='q':
        print('Goodby')
        break
    city=input('Entry you city:')
    if city.lower()=='q':
        print('Goodby')
        break
    singler_des=make_album(country,city)
    print('\n'+str(singler_des))

