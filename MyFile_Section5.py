
#1
# Start of my code
st = 'Print only the words that start with s in this sentence'

#print st

for i in st.split(' '):
	if i.startswith('s'):
		print i
		
#print st1[0]


#2
for num in range(11):
	if num % 2 ==0:
		print num

#3		
lst1 = [number for number in range(50) if number % 3 ==0]
print lst1
	
#4
st  = 'Print every word in this sentence that has an even number of letters'

for word in st.split(' '):
	if len(word) % 2 == 0:
		print word + ' even!'

#5
for num in range(1,100):
	if num % 3 == 0 and num % 5 == 0:
		print 'FizzBuzz'
	elif num % 3 == 0:
		print 'Fizz'
	elif num % 5 == 0:
		print 'Buzz'
	else:
		print num
		
		
#6
st = 'Create a list of the first letters of every word in this string'

lst = st.split(' ')

lst1 = [letter[0] for letter in lst]
print lst1