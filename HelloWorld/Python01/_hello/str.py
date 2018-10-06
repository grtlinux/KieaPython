# file: str.py

s = ''
str1 = 'Python is Great!'
str2 = "That's good"
str3 = 'Dont\'t walk'
str4 = 'That"s not good'
long_str = 'long line \
  ..continue..'

multiple_lines1 = '''
   first line
   second line
   third line
'''

multiple_lines2 = """
	Hello world!!!
	Who are you?
	What time is it?
	Are you crazy?
"""

s = 'spam and egg'
s = s[:5] + 'cheese ' + s[5:]

names = ['Lee','Youn']
for name in names:
	print '%s hello, world!!..' % name

a = 456
print '%d -- %o -- %x -- %X' % (a, a, a, a)

print str1
print str2
print str3
print str4
print long_str

print multiple_lines1
print multiple_lines2

print s

print '----------'

print '%(name)s -- %(phone)s' % {'name':'Kiea Seok Kang', 'phone':'010-4258-2025'}
name = 'gslee'
print vars()

print '----------'
s = ''
for k in range(100):
	s += 'spam'
print s

print '----------'
t = []
for k in range(100):
	t.append('spam')
s = ''.join(t)
print s

print '----------'
# unicode
print u'Spam and Egg'
print u'Spam \uB610 Egg'

print '----------'
# list
lt = [('one', 1), ('two', 2)]
for t in lt:
	print 'name=', t[0], 'num=', t[1]

for t in lt:
	print 'name=%s, num=%s' % t

for name, num in lt:
	print name, num

print '----------'
def mycmp(a1, a2):
	return cmp(a2, a1)

L = [1, 5, 3, 2, 4, 6]
L.sort(mycmp)
print L

print '----------'
L = [k * k for k in range(10)]
print L

L = []
for k in range(10):
	L.append(k * k)
print L

print '----------'
# inner list
L = [(i, j, i*j) for i in range(2, 100, 2) for j in range(3, 100, 3) if (i + j) % 7 == 0]
print L

print '----------'
# recursive
GNU = ['is not Unix']
GNU.insert(0, GNU)
print GNU

print '----------'
print dir()
A = [0] * 10
print A

print '----------'
# matrix
mat = [[1,2,3],
	[4,5,6],
	[7,8,9]]
print mat[1][2]

print '----------'
# tuple
t = 1, 2, 'hello'    # packing
x, y, z = t          # unpacking
print x, y, z

def calc(a, b):
	return a+b, a*b
x, y = calc(5, 4)
print x, y

print 'id:%s, name:%s' % ('gslee', 'Kiea')

def f(*args):
	print args
f(1, 2, 3)
f(1, 2, 3, 'spam', 'and', 'ham')

print '----------'
print '----------'
print '----------'
print '----------'
print '----------'
print '----------'
print '----------'
print '----------'
print '----------'
print '----------'
print '----------'



