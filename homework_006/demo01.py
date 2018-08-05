
#loop one
print('\n')
with open('learning_python.txt') as python_learn01:
    print(python_learn01.read().rstrip())
#Second read
print('\n')
with open('learning_python.txt') as python_learn02:
    for line in python_learn02:
        print(line.rstrip())
#Third read
print('\n')
with open('learning_python.txt') as python_learn03:
    lines=python_learn03.readlines()
    for line in lines:
        print(line.rstrip())

#Second ti
print('\n')
with open('learning_python.txt') as python_learn04:
    lines=python_learn04.readlines()
    for line in lines:
        r_line=line.replace('python'.title(),'C')
        r_line02=r_line.replace('python','C')
        print(r_line02.rstrip())
