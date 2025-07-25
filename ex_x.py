# Create a function that receives a string and prints "Hello, <the string>"

# Read the string from the terminal (input)

# If the input name is gkik respond with "Hello, Gkik", else respond with "Hello stranger"

name= input("Enter your name:")

##### HERE WE DEFINE THE FUNCTION ####
######################################
def greet(x):
  print ("Hello", x)
######################################


# HERE WE CALL THE FUNCTION #
######################################
greet(name)
#####################################

if name=="Gkik":
  print ("Hello big guy!")

else:
  print ("Hello stranger.")