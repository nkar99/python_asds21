import argparse

parser = argparse.ArgumentParser()
parser.add_argument('text', help = 'any text', type = str)
parser.add_argument('first_word', help = 'the word to be replaced with', type = str)
parser.add_argument('second_word', help = 'the word to replace with', type = str)
args = parser.parse_args()

new_string = args.text.replace(args.first_word,args.second_word)

print('The given text: ', args.text)
print('First word: ', args.first_word)
print('Second word: ', args.second_word)
print('Output string: ', new_string)