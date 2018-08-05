import json

def get_stored_username(filename):
    try:
        with open(filename) as f_obj:
            username=json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return username

def get_new_username(filename):
    username=input('Please input you username:\n')
    with open(filename,'w') as f_obj:
        json.dump(username,f_obj)
    return filename

def greet_user(filename):
    username=get_stored_username(filename)
    if username:
        while True:
            centery=input('You name is '+username+'? Please entry Y/N:')
            if centery.lower() in ['y','n']:
                break
        if centery.lower()=='y':
            print('Welcome back:'+username)
        else:
            get_new_username(filename)
    else:
        username=get_new_username(filename)
        print('We\'ll remember you when you come back,'+username+'!')

filename='username.json'
greet_user(filename)
