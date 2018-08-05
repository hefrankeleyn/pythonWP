import json

file_name='love_number.txt'
try:
    with open(file_name,'r') as num_file:
        love_num=json.load(num_file)
    print('love_num:'+str(love_num))
except FileNotFoundError:
    print('File is not found.')
        
