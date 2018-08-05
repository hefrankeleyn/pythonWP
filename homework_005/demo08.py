from collections import OrderedDict
favorite_languages=OrderedDict()

favorite_languages['java']='good java'
favorite_languages['c++']='good c++'
favorite_languages['python']='good python'

for language,lan_des in favorite_languages.items():
    print(language.title()+'\t'+lan_des.title())
