import json

while True:
    love_num=input('Please entry you love number:\n')
    try:
        int_love_num=int(love_num)
        break
    except ValueError:
        print('Please input a number!')
file_name='love_number.txt'
with open(file_name,'w') as num_file:
    json.dump(int_love_num,num_file)
