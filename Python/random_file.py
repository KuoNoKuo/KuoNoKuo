import random
#----------------------------------------------#
#When you want to use the moodule you will have to define the module first
random.
#----------------------------------------------#
#then you choose the function you want from the module:
#----------------------------------------------#
#for example; in order to randomly choose a number between two integers: randint
random.randint
#----------------------------------------------#
#then in the parameters you write the integers
random.randint(1,100)
# Randomly chooses a number between 1 and 100
#----------------------------------------------#
# You can assign a variable to the function if you want
RandomNumber_Variable = random.randint(1,100)
#----------------------------------------------#
# You can utilize the variable if you want or directly use the function
RandomNumber_Variable = random.randint(1,100)
print(RandomNumber_Variable)

print(random.randint(1,100))
#----------------------------------------------#
names = ['james','joshua','Sarah']
print(random.choice(names))
#----------------------------------------------#
print(random.random)