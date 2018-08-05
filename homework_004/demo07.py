def show_foods(*foods):
    print(foods)

show_foods('a_food','b_food','c_food')
show_foods('e_food')


print('\n')

def build_profile(first,last,**userinfo):
    profile={}
    profile['first']=first
    profile['last']=last
    for key,value in userinfo.items():
        profile[key]=value
    return profile
    
profile=build_profile('li','fei',school='tiannong',dream='gongjiangshi')
print(profile)

def cat_info(compay,id_num,**args):
    catInfos={}
    catInfos['compay']=compay
    catInfos['id_num']=id_num
    for key,value in args.items():
        catInfos[key]=value
    return catInfos=

print('\n')
car=cat_info('subaru','outback',color='blue',tow_package=True)
print(car)
