sentence = "Especially in electronic communications, writing in all caps is equivalent to yelling."
print(sentence.upper())

word_list = ["Simple","is","better","than","complex."]
print(" ".join(word_list))

sentence = "If the implementation is hard to explain, it might be a bad idea."
print(sentence.replace("hard","easy").replace("bad","good"))

print("Repetition" * 15) #repeatition in string

poem = """Whitecaps on the bay:
A broken signboard banging
In the April wind."""

print("beach" not in poem) #find a word in string

print(len("electroencephalographist")) #length of string