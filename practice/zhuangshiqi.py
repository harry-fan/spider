def dec1(func):  
    print("1111")# 2 
    def one():  
        print("2222")# 3  
        func()  
        print("3333")# 7
    return one  

def dec2(func):  
    print("aaaa")# 1 
    def two():  
        print("bbbb")# 4
        func()  
        print("cccc")# 6
    return two  

@dec1  
@dec2  
def test(): # 函数执行的顺序， 
    print("test test")# 5


test()  
