# Before

class A:
  pass

class B:
  def __init__(self):
    self.a_obj = A()
    
if __name__=="__main__":
  b_obj = B()
    
    
# after

class A:
  pass

# delegating object creation responsibility of other class outside
class B:
  def __init__(self,obj:A):
    self.a_obj = obj
    
if __name__=="__main__":
  a_obj = A()
  b_obj = B(a_obj)
  
  
# advanced use adding dependency inversion
from abc import ABC

class C(ABC):
  pass

class A(C):
  pass

class D(C):
  pass

class B:
  def __init__(self,obj:C):
    self.obj = obj
    
if __name__=="__main__":
#   delegate object creation responsibility outside B class
  a_obj = A()
  d_obj = D()
  b_obj = B(a_obj)
  b_obj2 = B(d_obj)

    
  
    
 
