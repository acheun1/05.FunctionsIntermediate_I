#Functions Intermediate I 
#2018 09 14
#Cheung Anthony

# As part of this assignment, please create a function randInt() where
# •	randInt() returns a random integer between 0 to 100
# •	randInt(max=50) returns a random integer between 0 to 50
# •	randInt(min=50) returns a random integer between 50 to 100
# •	randInt(min=50, max=500) returns a random integer between 50 and 500
# Create this function without using random.randInt() but you are allowed to use random.random().


import random
def randInt(min='', max=''):
    newmin=str(min)
    newmax=str(max)
    if not newmin.strip() and not newmax.strip():
        print("both min and max blanky", max)
        return(abs(round((random.random()*100))))
    elif not newmin.strip() and newmax.strip():
        print("max not blanky and min blanky", max)   
        return(abs(round((random.random()*max)))          )
    elif newmin.strip() and not newmax.strip():
        print("min not blanky and max blanky", min) 
        return(abs(round((random.random()*min-100))))
    else:
        print("both not blanky")
        return(abs(round((random.random()*min-max))))
print(randInt())
print(randInt(max=50))
print(randInt(min=50))
print(randInt(min=50, max=500))