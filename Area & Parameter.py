def Circle():
  r = int(input())
  a = 3.142*r*r
  p = 2*3.142*r
  print("Area:",a)
  print("Perimeter",p)
  return 0
 
def Square():
  r = int(input())
  a = r*r
  p = 4*r
  print("Area:",a)
  print("Perimeter",p)
  return 0

def Rectangle():
  l = int(input())
  b = int(input())
  a = l*b
  p = 2*(l+b)
  print("Area:",a)
  print("Perimeter",p)
  return 0

print("OPTIONS:\n1:Circle\n2:Square\n3:Rectangle\n4:Exit")
opt = int(input())
if opt==1:
  c = Circle() 
elif opt==2:
  c = Square()
elif opt==3:
  c = Rectangle()
else:
  print("Invalid")





