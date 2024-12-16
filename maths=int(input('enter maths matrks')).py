maths=int(input('enter maths marks'))
phy=int(input('enter phy marks'))
chem=int(input('enter chem marks'))
total_marks=600
sum_marks=maths+phy+chem
per=(sum_marks/total_marks)*100
print(per)
if per<35:
    print('grade is f')
elif per>35 and per<=50:
    print('grade is c')
elif per in range(51,91):
    print('grade is b')
elif per in range(91,101):
    print('grade is a')
else:
    print('invalid per')