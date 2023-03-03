

height = 145
credits = 9
with_taller_person = False

if height >= 137 or credits >= 10 :
  print('Enjoy the ride')
elif height < 137 or not with_taller_person:
  print('You are not tall enough to ride')
elif height >=100  and with_taller_person:
  print('Enjoy your the ride')
elif credits < 10: 
  print('You dont have enough credits to ride.')
else :
  print('Invalid data.')


