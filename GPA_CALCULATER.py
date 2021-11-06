enter_grade=0
enter_grade5=0
enter_grade4=0
b=int(input())
enter_grade2=input(str())
a=int(input())
enter_grade1=input(str())
enter_grade3=input(str())
c=int(input())
total=a+b+c
if enter_grade1== 'A'  :
    enter_grade=(int(4.00)*a)/a
elif enter_grade1=='A2':
    enter_grade=(3.67*a)/a

elif enter_grade1=='B1':
        enter_grade=3.33*a/a
        
elif enter_grade1=='B':
        enter_grade=3.0*a/a
        
elif enter_grade1=='B2':
        enter_grade=2.67*a/a
        
elif enter_grade1=='C1':
        enter_grade=2.33*a/a
    
elif enter_grade1=='C':
            enter_grade=2.0*a/a 
        
elif enter_grade1=='C2':
            enter_grade=1.67*a/a
elif enter_grade1=='D1':
    enter_grade=1.33*a/a
elif enter_grade1=='D':
    enter_grade=1.00*a/a
else:
    enter_grade=5*a/a


if enter_grade3== 'A' :
    enter_grade5=4.00*c/c
elif enter_grade3=='A2':
    enter_grade5=(3.67*c)/c

elif enter_grade3=='B1':
        enter_grade5=3.33*c/c
        
elif enter_grade3=='B':
        enter_grade5=3.0*c/c
        
elif enter_grade3=='B2':
        enter_grade5=2.67*c/c
        
elif enter_grade3=='C1':
        enter_grade5=2.33*c/c
    
elif enter_grade3=='C':
            enter_grade5=2*c/c
        
elif enter_grade3=='C2':
            enter_grade5=1.67*c/c
elif enter_grade3=='D1':
    enter_grade5=1.33*c/c
elif enter_grade3=='D':
    enter_grade5=1.00*c/c
else:
    enter_grade5=5*c/c
if enter_grade2== 'A' :
    enter_grade4=(int(4.00)*b)/b
elif enter_grade2=='A2':
    enter_grade4=(3.67*b)/b

elif enter_grade2=='B1':
        enter_grade4=3.33*b/b
        
elif enter_grade2=='B':
        enter_grade4=3.0*b/b
        
elif enter_grade2=='B2':
        enter_grade4=2.67*b/b
        
elif enter_grade2=='C1':
        enter_grade4=2.33*b/b
    
elif enter_grade2=='C':
            enter_grade4=2*b/b
        
elif enter_grade2=='C2':
            enter_grade4=1.67*b/b
elif enter_grade2=='D1':
    enter_grade4=1.33*b/b
elif enter_grade2=='D':
    enter_grade4=1.00*b/b
else:
    enter_grade2=5*b/b
sUm=(enter_grade+enter_grade4+enter_grade5)
total1=sUm/3
print(sUm)
print(total1)