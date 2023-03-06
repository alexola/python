

#Houses 

gryffindor = 0
hufflepuff = 0
ravenclaw = 0
slytherin = 0

print('Welcome to sorting the magic sorting hat 🦁 🦅 🦡 🐍')

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

answer = int(input('Enter answer (1-4): '))

if answer == 1:
  hufflepuff += 2
elif answer == 2:
  slytherin += 2
elif answer == 3:
  ravenclaw += 2
elif answer == 4:
  gryffindor += 2
else:
  print('Wrong input.')

#Q3
print('\nQ3) Which kind of instrument most pleases your ear?')

#Options

print('  1) The violin')
print('  2) The trumpet')
print('  3) The piano')
print('  4) The drum')

answer = int(input('Enter your answer (1-4): '))

if answer == 1:
  slytherin += 4
elif answer == 2:
  hufflepuff += 4
elif answer == 3:
  ravenclaw += 4
elif answer == 4:
  gryffindor += 4
else:
  print('Wrong input.')


#Results 

print("Gryffindor: ", gryffindor)
print("Ravenclaw: ", ravenclaw)
print("Hufflepuff: ", hufflepuff)
print("Slytherin: ", slytherin)
print(" ")
print("_____________")
print(" ")
#Explanation about the logic 
#Sorting out the logic basically it could be any house but remmeber the first if would start the filter.
#then reduce the options since it will start filtering thats why the first one got all the exceptions 
#Second one (1st elif ) would only compare the same value with the two remaining houses (huffelpuff amd slytherin) since gryffindor is out of the equation already 
#Third one would only compare the (2nd elif ) would only compare the last two remaining hufflepluff and slytherin 
#Else is for the remiaining one . You could start with slytherin or ravenclay or nay just need to apply the same logic 

if gryffindor >= ravenclaw and gryffindor >= hufflepuff and gryffindor >= slytherin:
  print('🦁 Gryffindor!')
elif ravenclaw >= hufflepuff and ravenclaw >= slytherin:
  print('🦅 Ravenclaw!')
elif hufflepuff >= slytherin:
   print('🦡 Hufflepuff!')
else:
   print('🐍 Slytherin!')
