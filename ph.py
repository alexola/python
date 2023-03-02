ph = int(input('Enter a pH vale (0-14):'))


if ph < 7:
  print("Base")
elif ph > 7:
  print("Acidic") 
else:
  print("Neutral")