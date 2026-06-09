# Sudent grade system.
Marks = 'M'
# M = 100
M = float(input("The current marks is: "))

if  M < 50:
    print ('The grade is F')
elif M >= 50 and M <= 59:
    print ("The grade is D")
elif M >= 60 and M <= 69:
    print ("The grade is C")
elif M >= 70 and M <= 79: 
    print ('The grade is B')
elif M >= 80 and M <= 100:
    print ('The grade is A')
else:
    print ('null')

# Electricity Bill
Unitsconsumed = 'X'
X = float(input("The unit consumed is: "))

if X > 300:
    print ('Kshs 25 per unit')
elif  X >= 201 and X <= 300:
    print ("Kshs 20 per unit")
elif X >= 101 and X <= 200:
    print ("Ksh 15 per unit")
elif X >= 0 and X <= 100: 
    print ('Kshs 10 per unit')
else: 
    print ("null")

# Movie ticet pricing.
Age = "D"
D = float(input("The age is: "))

if  D < 5:
    print ('Free')
elif D >= 5 and D <= 12:
    print ("The ticket goes for kshs 300")
elif D >= 13 and D <= 17:
    print ("The tcket goes for Kshs 500")
elif D>= 18 and D <= 59: 
    print ('The ticket goes for Kshs 1000')
elif D >= 60:
    print ("The ticket goes for Kshs 700")
else: 
    print("null")

#Bank loan eligibility 
Monthlyincome = "S"
S = float(input("The Monthlyincome is: "))

if  S < 20000:
    print ('Not eligible')
elif S >= 20000 and S <= 49999:
    print ("Small loan")
elif S >= 50000 and S <= 99999:
    print ("Medium loan")
elif S >= 100000: 
    print ('Large loan')
else: 
    print('null')

# employee bonus

Yearsworked = "Y"
Y= float(input("The years worked is: "))

if  Y < 1:
    print ('The bonus is 0%')
elif Y >= 1 and Y <= 3:
    print ("The bonus is 5%")
elif Y >= 4 and Y <= 7:
    print ("The bonus is 10%")
elif Y >= 7: 
    print ('The bonus is 15%')
else:
    print("null")

# mobile data bundles
Amount = "F"
F= float(input("The amount paid is: "))

if  F == 10:
    print ('The bundle is 100MB')
elif F == 20:
    print ("The bundle is 250MB")
elif F == 50:
    print ("The bundle  is 1GB")
elif F == 100: 
    print ('The bundle is 3GB')
elif F >= 200:
    print (" The bunlde is 8GB")
else:
    print("invalid")