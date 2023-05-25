import pyfiglet, time, winsound
from subprocess import call
from AppOpener import *


def wait(num):
    time.sleep(num)

def line():
  print('================================================================')


Title = pyfiglet.figlet_format('Cmd Assistant')

for i in range(2):
  print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
  wait(0.5)
  line()
  wait(0.5)
  print('Loading')
  wait(0.5)
  line()
  winsound.PlaySound('sound.mp3', winsound.SND_FILENAME)
  wait(1.0)

print(Title)

wait(0.4)
line()

print("HI, I'AM YOUR CMD ASSISTANT\n")

def run():
  cmd = (str(input('How Can I Help You??\n\n')))
  rad = '\n:+:\nI Will Do That.'

  command = cmd.lower()

  # print(command)

  if command == 'hi':
    print('Hello')
  elif command == 'edge' or command == 'web':    
    print(rad)
    open("microsoft edge")
  elif command == 'calc':
    print(rad)
    call(["calc.exe"])
  elif command == 'note':
    print(rad)
    open("notepad")
  elif command == 'word':
    print(rad)
    open("word")
  elif command == 'paint':
    print(rad)
    open("paint")
  elif command == 'ps' or command == 'gimp':
    print(rad)
    open("gimp")
  elif command == 'exit' or command == 'bye' or command == 'salam':
    print('\n\nsalam')
    wait(0.8)
    exit()
  else:
    print("Sorry, I can't UnderStand?!")

while True:
  run()

wait(5)