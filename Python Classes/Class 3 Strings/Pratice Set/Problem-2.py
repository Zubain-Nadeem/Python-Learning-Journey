a = input('Enter your name ')

letter = '''
Dear <|Name|>,
You are selected!
<|Date|>
'''
letter = letter.replace('<|Name|>' , a)
letter = letter.replace('<|Date|>' , '20-Oct-2026')


print(letter)

