# ~ username=input('Please entry you name:')
# ~ with open('guest.txt','w') as guest_file:
    # ~ guest_file.write(username)

while True:
    username=input('Please entry you name,or input "q" quit:')
    if username.lower()=='q':
        break
    with open('guest_book.txt','a') as guest_file:
        guest_file.write(username+'\n')
