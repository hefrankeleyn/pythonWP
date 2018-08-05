files=['cats.txt','dogs.txt','cd.txt']
for file_name in files:
    try:
        with open(file_name) as one_file:
            print(one_file.read())
    except FileNotFoundError:
        #print('The '+file_name+' is not found.')
        pass
