word=input('Please input a world:')
try:
    with open('ebook.txt') as ebook:
        content=ebook.read()
        num=content.count(word)
        num_lower=content.lower().count(word)
    print('num:'+str(num))
    print('num_lower:'+str(num_lower))
except FileNotFoundError:
    print('Not find the file.')
 
