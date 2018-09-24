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

# import random
# def randInt(min='', max=''):
#     newmin=str(min)
#     newmax=str(max)
#     if not newmin.strip() and not newmax.strip():
#         print("both min and max blanky")
#         return(round((random.random()*100)))
#     elif newmin.strip() and not newmax.strip():
#         print("min not blanky and max blanky", min) 
#         return(round((random.random()*100-min))) 
#     elif not newmin.strip() and newmax.strip():
#         print("max not blanky and min blanky")   
#         return(round((random.random()*max-50)))              
#     else:
#         print("both not blanky")
#         return(round((random.random()*max-min)))
# print(randInt())
# print(randInt(max=50))
# print(randInt(min=50))
# print(randInt(min=50, max=500))

#FUNCTIONING logic
# def randInt(min='', max=''):
#     newmin=str(min)
#     newmax=str(max)
#     if not newmin.strip() and not newmax.strip():
#         print("both min and max blanky")
#     elif newmin.strip() and not newmax.strip():
#         print("min not blanky and max blanky")  
#     elif not newmin.strip() and newmax.strip():
#         print("max not blanky and min blanky")        
#     else:
#         print("both blanky")
# print(randInt(max=2))
# print(randInt())
# print(randInt(min=2))

# import random
# def randInt(min='', max=''):
#     newmin=str(min)
#     newmax=str(max)
#     if (newmin and newmin.strip()) and (newmax and newmax.strip()):
#         return(random.random()*100-0)
#     else:
#         return("min or max not blank")
# print(randInt())


# import random
# def randInt(min='', max=''):
#     newmin=str(min)
#     newmax=str(max)
#     if newmin and newmin.strip() and newmax and newmax.strip():
#         print("not blank")
#     else:
#         return(random.random()*100-0)
# print(randInt())


# def randInt(min='', max=''):
#     newmin=str(min)
#     if newmin and newmin.strip():
#         print("not blank")
#     else:
#         print("blanky")
# print(randInt(min=2))


# import random

# def randInt(min=None, max=None):
#     max=float(max)
#     return(random.random()*max)
# print(randInt(max=2))



    # return(random.random()*min-max)
# print(randInt(min=1,max=2))
# print(randInt(min=,max=2))


# def isNotBlank (myString):
#     if myString and myString.strip():
#         #myString is not None AND myString is not empty or blank
#         return True
#     #myString is None OR myString is empty or blank
#     return False