


total = 0
add_more = True


while add_more == True:
      operator = input('input your operator: ')
      number = int(input('Enter a number: '))
      if operator == '+':
            total = total + number
      elif operator == '-':
            total = total - number
      elif operator == '*':
            total = total * number
      elif operator == '/':
            total = total / number

      print ('Total =',total)
      answer = input("want to add more 'Y' or 'N' : ")
      if answer =='Y':
            add_more = True
      else:
            add_more = False
print('Here is your total:', total)
      