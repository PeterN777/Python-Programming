Grossincome = "A"
A = 9500

if A < 5999:
    print ("B=150")
elif A >= 6000 and A <= 7999:
    print ("B=300")
elif A >= 8000 and A <=11999:
    print ("B=400")
elif A >= 12000 and A <=14999: 
    print ("B=500")
elif A >= 15000 and A <= 19999:
    print ("B=600")
elif A >= 20000 and A <=24999:
    print ("B=750")
elif A >= 25000 and A <=29999: 
    print ("B=850")
elif A >= 30000 and A <= 49999:
    print ("B=1000")
elif A >= 50000 and A <=99999:
    print ("B=1500")    
else:
    print("B=2000")