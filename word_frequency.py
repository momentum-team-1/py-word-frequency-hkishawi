

STOP_WORDS = [
    'a', 'an', 'and', 'are', 'as', 'at', 'be', 'by', 'for', 'from', 'has', 'he',
    'i', 'in', 'is', 'it', 'its', 'of', 'on', 'that', 'the', 'to', 'were',
    'will', 'with'
]


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

punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
filename = 'seneca_falls.txt'
file = open("seneca_falls.txt", 'rt')
text = file.read()
file.close()
words = text.split()
import string
table = str.maketrans('', '', string.punctuation)
stripped = [w.translate(table) for w in words]
print(stripped[:50])

# words = [word.lower() for word in words]  
words = [w for w in words if not w in STOP_WORDS]
print(words[:50])

# def remove_from_text(text, words):
#     output = []
#     for element in text:
#         if element != STOP_WORDS:
#             output.append(element)
#     return output
# print(output)



# no_punc = ''
# for char in seneca:
#     if char not in punctuations: 
#         no_punc += char
# print(no_punc)

