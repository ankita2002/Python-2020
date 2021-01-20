
import random
print("\n\n\nOUTPUT:\n\n")
print('WELCOME TO PASSWORD GENERATOR.')
n=int(input('ENTER LENGTH OF PASSWORD'))
passwordlist= list()
password='  '
number=['0','1','2','3','4','5','6','7','8','9']
lowerc=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
upperc=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
characters=['!','@','#','$','%','^','&','*','(',')','_','-','+','|',':','?','/','<','>','~']
print('1.NUMBERS \n2.UPPERCASE\n3.LOWERCASE\n4.UPPERCASE+LOWERCASE\n5.CHARACTERS\n6.UPPERCASE+LOWERCASE+NUMBERS\n7.NUMBERS+CHARACTERS\n8.UPPERCASE+CHARACTERS\n9.LOWERCASE+CHARACTERS\n10.MIXED SET')
c=int(input('ENTER YOUR CHOICE:'))
if c==1:
    passwordlist += number
elif c==2:
    passwordlist += upperc
elif c==3:
    passwordlist += lowec
elif c==4:
    passwordlist += upperc + lowerc
elif c==5:
    passwordlist += characters
elif c==6:
    passwordlist += number + upperc + lowerc
elif c==7:
    passwordlist += number + characters
elif c==8:
    passwordlist += upperc + characters
elif c==9:
    passwordlist += lowerc + characters
elif c==10:
    passwordlist += number + characters + upperc + lowerc
for i in range (n):
    password += random.choice(passwordlist)
print('PASSWORD: ',password)



print('\n\n\n')