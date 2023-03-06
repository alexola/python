


gryffindor = 0
hufflepuff = 0
ravenclaw = 0
slytherin = 0

print('Welcome to sorting hat ')

#Q1 

print('Q1) Do you like Dawn or Dusk?')

#Options 

print('  1) Dawn')
print('  2) Dusk')

answer = int(input('Enter answer (1-2): '))

if answer == 1:
  gryffindor += 1
  ravenclaw += 1
elif answer == 2:
  slytherin += 1
  hufflepuff += 1
else: 
  print('Wrong input.')



#Q2

print("\nQ2) When I'm dead, I want people to remember me as:")

#Options 

print('  1) The Good')
print('  2) The Great')
print('  3) The Wise')
print('  4) The Bold')

#Q3
print('\nQ3) Which kind of instrument most pleases your ear?')

#Options

print('  1) The violin')
print('  2) The trumpet')
print('  3) The piano')
print('  4) The drum')