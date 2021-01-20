import time
print("START")
s=0
a=("ANKITA IS ANA, I AM SO DONE")
print(a) 
c=list(a.split(' ')) 
starttime=time.time() 
b=list(input().split(' ')) 
endtime=time.time() 
for i in range (len(b)):
   if c[i]==b[i]:
      s=s+1
result=endtime-starttime
print(s) 
print(result)
print("ACCURACY IS ",round((s/7)*100,2),"%")
