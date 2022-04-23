counts = dict()
print("Enter a text of line:")
line = input(" ")
words = line.split()
print("words", words)
print("counting.....")
for word in words:
    counts[word] = counts.get(word) + 1
print("counts", count)
