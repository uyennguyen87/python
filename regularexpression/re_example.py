'''
Created on Feb 22, 2016

@author: ncuyen
'''

""" This example follow http://www.python-course.eu/re.php """
import re

""" Let's start"""

text = "A cat and a rat can't be friends."
pattern = r'cat'
x = re.search(pattern, text)
print x

print
pattern = r'cow'
x = re.search(pattern, text)
print x

""" any character with '.' """
print
pattern = r'.at'
x = re.search(pattern, text)
print x

""" Character Classes
[xyz] means either an "x", an "y" or a "z"
[a-d] means [abcd]
[0-5] means [012345]
[a-z] means any lowercase
[A-Z] means any uppercase
[a-zA-Z] means normal character only
[0-9] means digit only
but [-az] or [az-] means either "-" or "a" or "z"

[^abc] means not a and b and c
but [a^bc] means a or ^ or b or c
"""
with open("simpsons_phone_book.txt") as phone_book:
    pattern = r'J.*Neu'
    for line in phone_book:
        if re.search(pattern, line):
            print line.rstrip()


""" Predefined Character Classes
\d means [0-9] means any decimal digit
\D means [^0-9] means any non-digit character
\s means [\t\n\r\f\v] means any whitespace character
\S means [^\t\n\r\f\v] means any non-whitespace character
\w means [a-zA-Z0-9_] means any alphanumeric character
\W means [^a-zA-Z0-9_] means the complements of \w
\b means the empty string but only at start or end of a word
\B means the empty string but not at start or end of a word
\\ means a literal backslash
"""

s1 = "Mayer is a very common Name"
s2 = "He is called Meyer but he isn't German."
s = s2 + '\n' + s1
pattern = r"^M[ae][iy]er"

print
print "re.search('%s', '%s')" % (pattern, s1)
print re.search(pattern, s1)


print
print "re.search('%s', '%s')" % (pattern, s2)
print re.search(pattern, s2)

print
print "re.search('%s', '%s')" % (pattern, s)
print re.search(pattern, s)

print
print "re.search('%s', '%s', re.MULTILINE)" % (pattern, s)
print re.search(pattern, s, re.MULTILINE)

print
print "re.search('%s', '%s', re.M)" % (pattern, s)
print re.search(pattern, s, re.M)

print
print "re.match('%s', '%s', re.M)" % (pattern, s)
print re.match(pattern, s, re.M)


pattern = r'Python\.$'
s1 = 'I like Python.'
s2 = 'I like Python and Perl.'
s3 = 'I like Python.\nSome prefer Java or Perl.'

print
print "re.search('%s', '%s')" % (pattern, s1)
print re.search(pattern, s1)

print
print "re.search('%s', '%s')" % (pattern, s2)
print re.search(pattern, s2)


print
print "re.search('%s', '%s', re.M)" % (pattern, s3)
print re.search(pattern, s3, re.M)

""" Quantify
*: 0-n
?: 0-1
+: 1-n
{a}: a
{a,b}: a-b
"""
pattern = r'[0-9]+'
text = "Customer number: 232454, Date: February 12, 2011"

print
print "mo = re.search('%s', '%s')" % (pattern, text)
mo = re.search(pattern, text)

print 
print 'mo.group()'
print mo.group()

print 
print 'mo.span()'
print mo.span()

print
print 'mo.start()'
print mo.start()

print
print 'mo.end()'
print mo.end()

pattern = r'([0-9]+).*: (.*)'

print
print "mo = re.search('%s', '%s')" % (pattern, text)
mo = re.search(pattern, text)

print 
print 'mo.group()'
print mo.group()

print 
print 'mo.group(1)'
print mo.group(1)

print 
print 'mo.group(2)'
print mo.group(2)


pattern = r"<([a-z]+)>(.*)</\1>"

print
with open("tags.txt") as f:
    for line in f:
        res = re.search(pattern, line)
        print res.group(1) + ': ' + res.group(2)



        
phone_list = ["555-8396 Neu, Allison", 
     "Burns, C. Montgomery", 
     "555-5299 Putz, Lionel",
     "555-7334 Simpson, Homer Jay"]
pattern = r'([0-9-]*)\s*([A-Za-z]+),\s+(.*)'
print
for phone_info in phone_list:
    res = re.search(pattern, phone_info)
    print res.group(3) + ' ' + res.group(2) + ' ' + res.group(1)

""" Named backreferences """
linux_date_str = "Sun Oct 14 13:47:03 CEST 2012"
pattern = r"\b(?P<hours>\d\d):(?P<minutes>\d\d):(?P<seconds>\d\d)\b"
print
res = re.search(pattern, linux_date_str)
print res.group('hours')
print res.group('minutes')
print res.start('minutes')
print res.end('minutes')
print res.span('seconds')
    