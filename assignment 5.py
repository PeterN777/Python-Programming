# a function to print all even numbers from 1 to n
def even (n):
        for n in range (1,n+1): 
          if n%2==0:
             print ("The number is even",n)
even (20)

# a function to print all odd numbers.
def odd (n):
    for n in range (1,n+1):
        if n%2==1:
            print('This is an odd number',n)
odd(10)