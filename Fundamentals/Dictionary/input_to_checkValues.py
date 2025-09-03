exam_marks = {'Cierra Vega': 175, 'Alden Cantrell': 200, 'Kierra Gentry': 165, 'Pierre Cox': 190}
num=int(input('Enter the marks to check: '))
name = 'None'
for key in exam_marks:

  if exam_marks[key] == num:
   name = key
   break
 
  
print(f'{num} marks is scored by {name}.')


