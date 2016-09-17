
import re

line = 'From: shaptala@itstep.org Sat Jan  5 09:14:16 2016'

email = re.findall(r'(\S+)@(\S+)', line)
print(email)

at = line.find('@')
print(at)
space = line.find(' ', at)
print(space)
