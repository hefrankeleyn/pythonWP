def show_magicians(magicians):
    for magician in magicians:
        print(magician.title())

magicians=['a_m','b_m','c_m']
show_magicians(magicians)
print('\n')
def make_great(magicians):
    for m_i in range(len(magicians)):
        magicians[m_i]='the Great '+magicians[m_i]
    return magicians
        

magicians_clone=make_great(magicians[:])
show_magicians(magicians)
show_magicians(magicians_clone)
