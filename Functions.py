# Having functions removes repetitive code, as the function's purpose can be used multiple times throughout a program.
def sayHello(name):
     print("Hello " + name + "! Nice to meet you.")

sayHello("ben") # Output is: Hello Ben! Nice to meet you



# A function can also return a result, see the code block below:
def calcCost(item):
     if(item == "sweets"):
          return 3.99
     elif (item == "oranges"):
          return 1.99
     else:
          return 0.99

spent = 10
spent = spent + calcCost("sweets")
print("You have spent:" + str(spent))
