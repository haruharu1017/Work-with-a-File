text = input('enter the text: ')

t = ''.join(text.split())
txt = list(t)

txt.reverse()
new = ''.join(txt)

if new == t:
    print('palindrome: ' + text)
else:
    print('not a palindrome: ' + text)






