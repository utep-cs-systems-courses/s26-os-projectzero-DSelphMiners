#!/usr/bin/env python3

import re

file = "speech.txt"
reading = open(file, buffering = 1024, mode = 'r', encoding='utf-8')

#print(reading.buffer.__sizeof__())

#read each word into a hashtable that increase the count of each word
words = {}
for line in reading:
    for word in re.findall(r'\b\w+\b', line):
        word = word.lower()
        words[word] = words.get(word, 0) + 1

#write the hashtable to a .txt file
word_count = open("word_count.txt", mode = 'w', encoding='utf-8')
for word in sorted(words):
    word_count.write(word + " " + str(words[word]) + "\n")

#close the file we read in
reading.close()
word_count.close()
