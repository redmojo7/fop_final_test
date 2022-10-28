import re

addressRegex = re.compile(r'''(
(\d+\w?)([\s\w+]+),((\s\w+)+),\s(\d+)
 )''', re.VERBOSE)
fileobj = open('addresses.txt')
data = fileobj.readlines()
for address in data:
    address = address.strip()
    mo = addressRegex.search(address)
    if mo:
        # print('Found: ' + mo.group())

        print('Found: ' + mo.group(2) + mo.group(3) + mo.group(4) + " " + mo.group(6))

templist = ['74', '34', '284', '290']

integerlist = [int(str) for str in templist]
print(integerlist)

wordlist = ['FUNDAMENTALS', 'of', 'programming']
titlecase = [word[0].upper() for word in wordlist]
print(titlecase)

years = [1990, 1900, 1980, 1950, 1985, 2000, 1988]
eighties = [year for year in years if 1980 <= year <= 1989]
print(eighties)
