a= format( 'Body Mass Index','^180')
print (a)
print ("Body Mass Index / BMI determine that , how much fat a person has \n BMI= kg/(m^2)")
kg= float(input("Enter your weight in kilogram : "))
m= float(input("Enter your height in meter : "))
m2= m**2
BMI= kg/m2
if BMI<18.5:
     print (" Your BMI is = \t", BMI ,"\n '''You are Underweight'''")
elif BMI<22:
     print (" Your BMI is = \t", BMI , "\n '''You are Normal'''")
elif BMI<24:
     print (" Your BMI is = \t", BMI , "\n '''You are Overweight'''")
else:
     print (" Your BMI is = \t", BMI , "\n '''Obesity! Should Consult a Doctor!'''")

question= str(input ("\n\nDo You want more BMI calculation [yes / no]: "))
if question=="yes":
     def my_command():
          # Your command or code here
          print("\n\n\n For more BMI calculations ->>>")
          kg= float(input("Enter your weight in kilogram : "))
          m= float(input("Enter your height in meter : "))
          m2= m**2
          BMI= kg/m2
          if BMI<18.5:
               print (" Your BMI is = \t", BMI ,"\n '''You are Underweight'''")
          elif BMI<22:
               print (" Your BMI is = \t", BMI , "\n '''You are Normal'''")
          elif BMI<24:
               print (" Your BMI is = \t", BMI , "\n '''You are Overweight'''")
          else:
               print (" Your BMI is = \t", BMI , "\n '''Obesity! Should Consult a Doctor!'''")
          question= str(input ("\n\nDo You want more BMI calculation [yes / no]: "))
          if question=="yes":
               def my_command():
                    # Your command or code here
                    print("\n\n\n For more BMI calculations ->>>")
                    kg= float(input("Enter your weight in kilogram : "))
                    m= float(input("Enter your height in meter : "))
                    m2= m**2
                    BMI= kg/m2
                    if BMI<18.5:
                         print (" Your BMI is = \t", BMI ,"\n '''You are Underweight'''")
                    elif BMI<22:
                         print (" Your BMI is = \t", BMI , "\n '''You are Normal'''")
                    elif BMI<24:
                         print (" Your BMI is = \t", BMI , "\n '''You are Overweight'''")
                    else:
                         print (" Your BMI is = \t", BMI , "\n '''Obesity! Should Consult a Doctor!'''")
                    # You can call the function multiple times to "restart" it
                    for _ in range(10000):
                         my_command()
          else:
               print("Thank you for using this program!")


     # You can call the function multiple times to "restart" it
     for _ in range(10000):
          my_command()
else:
     print("Thank you for using this program!")

