#4 variant
#task 1
s = str(input())
words = s.split(" ")
print(words)
longest_word = ""
max_length = 0
for i in words:
    if len(i) > max_length:
        max_length = len(i)
        longest_word = i
print("Самое длинное слово: ", longest_word)
print("Длина: ", max_length)
