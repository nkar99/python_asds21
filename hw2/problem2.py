import argparse

parser = argparse.ArgumentParser()
parser.add_argument('text', help = 'input a text with #of chars {>7, //2==1}', type = str)
parser.add_argument('--num_d', help = 'the number of days', type = int)
args = parser.parse_args()

text = args.text
l = int((len(text) - 3)/2)
mid_chars = text[l:len(text)-l]
new_text = text[:l] + mid_chars.upper() +text[len(text)-l:]

print('The old string:', args.text)
print('Middle 3 characters: ', mid_chars)
print('The new string: ', new_text)
