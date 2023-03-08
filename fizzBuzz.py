
#Remember that you need to get a one digit more form the total
#In this example we wanted from  1 to 15 so we put on 16

for x in range(1,16):
  if(x % 3 == 0) and (x % 5 == 0):
    print('FizzBuzz')
  elif(x % 3 == 0):
    print('Fizz')
  elif(x % 5 == 0):
    print('Buzz')
  else:
    print(x)  
  
  