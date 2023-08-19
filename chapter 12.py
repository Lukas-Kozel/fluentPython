class   DoppelDict(dict):
    def __setitem__(self,key, value) -> None:
        return super().__setitem__(key, [value]*2)
    

dd = DoppelDict(one=1)
print(dd)
dd['two'] = 2
print(dd)
dd.update(three=3)
print(dd)


class A:
    def ping(self):
        print("ping: ",self)


class B(A):
    def pong(self):
        print("pong: ",self)


class C(A):
    def pong(self):
        print("PONG: ",self)
        

class D(B, C):
    
    def ping(self):
        super().ping()
        print("post-ping: ",self)
    
    def pingpong(self):
        self.ping()
        super().ping()
        self.pong()
        super().pong()
        C.pong(self)
        
d=D()
d.pong()
C.pong(d)
