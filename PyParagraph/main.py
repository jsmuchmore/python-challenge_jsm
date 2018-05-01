file = open("resources\paragraph_1.txt")

paragraph_words=[]
paragraph_sentences=[]

sentences = 0

for line in file:
    print("Line:" + line)
    for word in line.split(" "):
        paragraph_words.append(word)

        words = len(paragraph_words)

for line in file:
    print("Line:" + line)
    for sentence in line.split("."):
        print("Sentence: " + sentence)
        paragraph_sentences.append(sentence)

        sentences = len(paragraph_sentences)


word_lengths = [len(i) for i in paragraph_words]

for i in paragraph_words:
    word_lengths = [len(i)]

average_word_lengths = (sum(word_lengths))/words


print(average_word_lengths)
print(word_lengths)

print(paragraph_sentences)
#print (words)
#print(sentences)

file.close()
