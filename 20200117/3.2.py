def print_string(*strs, **kw):
    sep = ' '
    if 'sep' in kw:
        sep = kw['sep']
    str = sep.join(strs)
    end = '\n'
    if 'end' in kw:
        end = kw['end']
    print(str + end)

print_string('This is a test')
print_string('This', 'is', 'a', 'test')
print_string('This', 'is', 'a', 'test', sep = '-')
print_string('This', 'is', 'a', 'test', ',', 'Yes', sep = '_', end = '.')
