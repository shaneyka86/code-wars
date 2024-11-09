#even or odd
#def even_or_odd(number):
  # if number % 2 == 0:
  #  return 'Even'
 #  else:
   # return 'Odd'

#count the vowels
import string


def getCount(string):
   vowels = 'aeiou'
   count = 0
   for char in string:
      if char in vowels:
         count += 1
      return count