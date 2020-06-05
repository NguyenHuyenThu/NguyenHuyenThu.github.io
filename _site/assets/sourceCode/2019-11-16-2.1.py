import re

line = 'asdf fjdk; afed, fjek,asdf,foo'

res = re.split(r'[;,\s]\s*',line)

print(res) # 