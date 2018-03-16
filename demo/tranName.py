import re

str = 'HasBeanCreationStarted'

strs = re.findall ('[A-Z][^A-Z]*', str)

r = ''
for a in strs:
    r = r + ' ' + a

print (r)
