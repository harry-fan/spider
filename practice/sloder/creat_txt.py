import os

def txt(name, text):
    b = os.getcwd()[:-6]
    print(b)

    if not os.path.exists(b):
        os.makedirs(b)
    
    xxoo = b + name + '.txt'
    f = open(xxoo, 'wb')
    f.write(text)

    f.close()
    print('over')

txt('xxoo', 'hello, python')
