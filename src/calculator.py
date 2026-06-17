class Calculator :
  def add ( self , a : int , b : int ) -> int :
    return a + b

  def subtract ( self , a : int , b : int ) -> int :
    return a - b

  def multiply ( self , a : int , b : int ) -> int :
    return a * b
    
  def div ( self , a : int , b : int ) -> float :
    if b == 0:
      raise VeError (" Cannot divide by zero ")
    return a / b