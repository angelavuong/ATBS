spam = ['apples','bananas','tofu','cats']
spam[-1] = 'and ' + spam[-1]
print ', '.join(map(str,spam))
