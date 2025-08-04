value = input('Enter the value of the item in format $$$$.cents: ')
try:
    valuefloat = float(value)
    parts = str(valuefloat).split('.')
    dollar = parts[0]
    cents = parts[1]
    print(f'Price is {dollar} dollars with {cents} cents')
except:
    print('Entered number has not the correct format')