def pigLatin(word):
	ending = ''
	x = ['a','e','i','o','u','y']
	if word[0] not in x:
		i = 0
		while word[i] not in x:
			ending += word[i]
			i+=1

		new_word = word[i:]+ending+'ay'
	if word[0] in x:
		new_word = word+'yay'
	return new_word


word = 'insert phrase here'
word = word.split()
output = ''

for x in range(len(word)):
	output += pigLatin(word[x])+' '

print(output)
