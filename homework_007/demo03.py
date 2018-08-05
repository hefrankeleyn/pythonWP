import json

def show_love_num(file_name):
    try:
        with open(file_name) as num_file:
            love_num=json.load(num_file)
        print('You love num is '+str(love_num))
    except FileNotFoundError:
        love_num=store_num_to_file(file_name)
        print('You love num is '+str(love_num))

def store_num_to_file(file_name):
    while True:
        try:
            love_num=input('Please entry you love num:\n')
            int_love_num=int(love_num)
            with open(file_name,'w') as num_file:
                json.dump(int_love_num,num_file)
            break
        except ValueError:
            print('Please input a number!')
    return int_love_num

show_love_num('num_file03.txt')

