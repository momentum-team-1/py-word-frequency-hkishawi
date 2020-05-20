

STOP_WORDS = [
    'a', 'an', 'and', 'are', 'as', 'at', 'be', 'by', 'for', 'from', 'has', 'he',
    'i', 'in', 'is', 'it', 'its', 'of', 'on', 'that', 'the', 'to', 'were',
    'will', 'with'
]
punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

def print_word_freq(file):
    """Read in `file` and print out the frequency of words in that file."""
    pass

print('hello world')

# if __name__ == "__main__":
#     import argparse
#     from pathlib import Path

#     parser = argparse.ArgumentParser(
#         description='Get the word frequency in a text file.')
#     parser.add_argument('file', help='file to read')
#     args = parser.parse_args()

#     file = Path(args.file)
#     if file.is_file():
#         print_word_freq(file)
#     else:
#         print(f"{file} does not exist!")
#         exit(1)


# filename = 'seneca_falls.txt'
# file = open("seneca_falls.txt", 'rt')
# text = file.read()
# file.close()
# words = text.split()
# import string

# REMOVING PUNCTUATIONS (not sure how this works)
# table = str.maketrans('', '', string.punctuation)
# stripped = [w.translate(table) for w in words]
# print(stripped[:50])

# REMOVING STOP WORDS
# # words = [word.lower() for word in words]  
# words = [w for w in words if not w in STOP_WORDS]
# print(words[:50])

# Attempt to REMOVE STOP WORDS (this does not work)
# def remove_from_text(text, words):
#     output = []
#     for element in text:
#         if element != STOP_WORDS:
#             output.append(element)
#     return output
# print(output)
# def clean_words():
# def remove_punc():

# THIS WORKS 
# no_punct = ""
# for char in text:
#     if char not in punctuations: 
#         no_punct += char
# print(no_punct[:500].lower())

# THIS SHOULD WORK
# def remove_stop(text):
# non_stop = []
# for word in words:
#     if word not in STOP_WORDS:
#         non_stop.append(word)

# TRIAL
# def word_count(text):
#     counts = dict()
#     words = text.split()

#     for word in words:
#         if word in counts:
#             counts[word] += 1
#         else: 
#             counts[words] = 1
#     return counts
# print(word_count(words))

# def count_words():
#     text = open("seneca_falls.txt", 'rt')
#     d = dict()
#     for line in text:
#         line = line.strip()
#         line = line.lower()
#         line = line.translate(line.make)
#         words = line.split(" ")
#         for word in words:
#             if word in d:
#                 d[word] = d[word] + 1
#             else:
#                 d[word] = 1
#     for key in list(d.keys()):
#         print(key, ":", d[key])

import string 

# Open the file in read mode 
text = open("seneca_falls.txt", "r") 

# Create an empty dictionary 
d = dict() 

non_stop = [] #words w stop words removed 

# Loop through each line of the file 
for line in text: 
	# Remove the leading spaces and newline character 
	line = line.strip() 

	# Convert the characters in line to 
	# lowercase to avoid case mismatch 
	line = line.lower() 

	# Remove the punctuation marks from the line 
	line = line.translate(line.maketrans("", "", string.punctuation)) 

	# Split the line into words 
	words = line.split(" ") 

# NEED TO INCORPORATE THIS
for word in words:
    if word not in STOP_WORDS:
        non_stop.append(word)

	# Iterate over each word in line 
	for word in words: 
		# Check if the word is already in dictionary 
		if word in d: 
			# Increment count of word by 1 
			d[word] = d[word] + 1
		else: 
			# Add the word to dictionary with count 1 
			d[word] = 1

# Print the contents of dictionary 
for key in list(d.keys()): 
	print(key, ":", d[key]) 
