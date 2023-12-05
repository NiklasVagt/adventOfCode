import re

digitsWords = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
digits = ['1','2','3','4','5','6','7','8','9']
sum = 0;


with open('input1.txt') as f:
  lines = f.readlines()
  for line in lines: 
    firstDigit = ''  
    lastDigit = ''
    indexFirst = len(line)
    indexLast = 0
    firstFound = len(line)
    lastFound = 0
    
    for digit in digitsWords:
      try:
        firstFound = line.index(digit)
        if(firstFound < indexFirst):
          indexFirst = firstFound
          firstDigit = digits[digitsWords.index(digit)]
      except:
        pass

      try:
        lastFound = line.rindex(digit)
        if(lastFound > indexLast): 
          indexLast = lastFound
          lastDigit = digits[digitsWords.index(digit)]
      except: 
        pass
    firstNumber = re.findall('[0-9]', line)[0]
    lastNumber = re.findall('[0-9]', line)[-1]

    ifIndexFirst = len(line)
    try:
      ifIndexFirst = line.index(digitsWords[digits.index(firstDigit)])
    except:
      pass

    ifIndexLast = 0
    try:
      ifIndexLast = line.index(digitsWords[digits.index(lastDigit)])
    except: 
      pass

    print(line)
    print(line.index(lastNumber))
    print(ifIndexLast)
    if(line.index(firstNumber) <= ifIndexFirst):
      firstDigit = firstNumber
    if(line.rindex(lastNumber) >= ifIndexLast):
      lastDigit = lastNumber      


    sum = sum + int(firstDigit+lastDigit)

  print(sum)