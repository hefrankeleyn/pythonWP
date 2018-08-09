import re

fee_str='''
[{"fee":"600","integrateitem":"月固定费","parentitemcode":"-1","integrateitemcode":"1001"},
        {"fee":"600","integrateitem":"基本套餐费","parentitemcode":"1001","integrateitemcode":"21229"},
        {"fee":"370","integrateitem":"增值业务费","parentitemcode":"-1","integrateitemcode":"1002"},
        {"fee":"0","integrateitem":"增值业务-绿色邮箱","parentitemcode":"1002","integrateitemcode":"436789"},
        {"fee":"370","integrateitem":"承诺话费补足费用","parentitemcode":"1002","integrateitemcode":"110142"},
        {"fee":"30","integrateitem":"上网费","parentitemcode":"-1","integrateitemcode":"1009"},
        {"fee":"30","integrateitem":"手机上网流量费","parentitemcode":"1009","integrateitemcode":"21275"}]
'''
# ~ fee_regex=re.compile(r'''.*"(.*?)(","integrateitem":"月固定费)(")''')
fee_regex=re.compile(r'''.*"(.*?)(","integrateitem":"月固定费)(")''')

mo=fee_regex.search(fee_str)
#print(mo)
if mo:
    print(mo.group(0))
    print(mo.group(1))
    print('len(mo.groups())',len(mo.groups()))
    for i in mo.groups():
        print(i)
