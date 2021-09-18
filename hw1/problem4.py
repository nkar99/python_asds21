text = input('Please input text: ')
count = text.count('USA') + text.count('usa')
new_text = text.replace('USA','Armenia').replace('usa','Armenia') 

print('The given string:',text)
print('The USA/usa count is:', count)
print('The new string:',new_text)

