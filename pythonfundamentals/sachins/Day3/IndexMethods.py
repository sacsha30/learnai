word = "computer"
fifth = word[4]
print(fifth)

sentence = "In theory, theory and practice are the same. In practice, they are not."
print(sentence.index('practice'))

sentence = "In theory, theory and practice are the same. In practice, they are not."
print(sentence.rindex("practice")) #right index

sentence = "Controlling complexity is the essence of programming"
print(sentence[0:sentence.index(' ')]) #slicing first word