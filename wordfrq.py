punctuation = '~!@#$%^&*()_+{}|:"<>?`=[]\\;\',./'
filename = 'grimm.txt'
book = open(filename).read()
bookNoPunct = book.translate(str.maketrans('', '', punctuation))
words = bookNoPunct.split()
wordfreq = {}
for word in words:
    if not word.isnumeric() and word.lower() not in wordfreq:
        wordfreq[word.lower()] = 0
        wordfreq[word.lower()] += 1

print(len(wordfreq))

print(wordfreq.keys())
