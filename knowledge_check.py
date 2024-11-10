#even or odd
def even_or_odd(number):
   if number % 2 == 0:
    return 'Even'
   else:
    return 'Odd'

#count the vowels

def getCount(string):
   vowels = 'aeiou'
   count = 0
   for char in string:
      if char in vowels:
         count += 1
      return count
#number to string
def number_to_string(num):
    return str(num)