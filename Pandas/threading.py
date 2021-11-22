import threading #多執行緒

class MyClass(threading.Thread):#繼承
    def __init__(self,x):
        threading.Thread.__init__(self)
        self.str = x
    def run(self):#程式
        for i in range(10):
            print (i,self.str + "\n")
        
        
        
#實行程式
MyClass("a").start()
MyClass("b").start()
print()

