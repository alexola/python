import random

print('Ask me anything you want:')
question = input()

rnum = random.randint(1, 9)

if rnum == 1:
  amnswer = 'Yes - definitely.'
elif rnum == 2:
  answer = 'It is decidedly so.'
elif rnum == 3:
  answer = 'Without a doubt.'
elif rnum == 4:
  answer = 'Reply hazy, try again.'
elif rnum == 5:
  answer = 'Ask again later.'
elif rnum == 6:
  answer ='Better not tell you now.'
elif rnum == 7:
  answer = 'My sources say no.'
elif rnum == 8:
  answer = 'Outlook not so good.'
elif rnum == 9:
  answer = 'Very doubtful'
else:
  answer = 'Error , please try again.'

print('Question   ' + question)
print('MagicBall 8 :   ' + answer)