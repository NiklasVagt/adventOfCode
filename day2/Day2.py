import re



def taskOne():
  cubes = {
    'red': 12,
    'green': 13,
    'blue': 14
  }
  sum = 0
  with open('input.txt') as f:
    lines = f.readlines()
    for line in lines:
      possible = True
      id = re.findall('[0-9]+', line)[0]
      list = line[line.index(':')+2:len(line)-1].split('; ')
      for grab in list:
        grab = grab.split(', ')
        for color in grab:
          cubeColor = re.search('[a-z]+', color).group()
          cubeNumber = re.search('[0-9]+', color).group()
          if(int(cubeNumber) > cubes[cubeColor]):
            possible = False
      if(possible):
        sum += int(id)
    print(sum)

def taskTwo():
  sum = 0
  with open('input.txt') as f:
    lines = f.readlines()
    for line in lines:
      cubes = {
        'red': 0,
        'green': 0,
        'blue': 0
      }
      list = line[line.index(':')+2:len(line)-1].split('; ')
      for grab in list:
        grab = grab.split(', ')
        for color in grab: 
          cubeColor = re.search('[a-z]+', color).group()
          cubeNumber = re.search('[0-9]+', color).group()
          if(int(cubeNumber) > cubes[cubeColor]):
            cubes[cubeColor] = int(cubeNumber)
      sum += cubes['red']*cubes['green']*cubes['blue']
    print(sum)

taskTwo()