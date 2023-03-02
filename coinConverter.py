# Writing a convertor from different currencies 
# From Their original value to euro 

a = int(input( 'What do you have left in yuan? '))
b = int(input('What do you have left in yen? '))
c = int(input('What do you have left in won? '))



yuan = a * 0.14 # val = 15  res= 2.10
yen = b * 0.0069 #val = 15  res = 0.1035
won = c * 0.00072 #val = 15 res = 0.0108

total = yuan + yen + won 
print(total)
