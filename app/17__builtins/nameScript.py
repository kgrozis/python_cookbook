# PROBLEM:  Why is the __name__ variable used?
# SOLUTION: Can import scripts as a module in another script.  Can use name
#           to decide if you want to run script
#           When you run your script __name__ var equals __main__ var

def myFunction():
  print(f"The value of __name__ is {__name__}")

def main():
  myFunction()

# when imported this statement is false
if __name__ == '__main__':
  main()