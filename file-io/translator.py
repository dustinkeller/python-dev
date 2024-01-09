from googletrans import Translator

try:
	with open('file-io/originals.txt', 'r') as f:
		text = f.read()
		translator = Translator()
except FileNotFoundError:
	print("Please make sure the original.txt file is in the file-io folder...")

with open('file-io/translated.txt', 'w') as f:
	f.write(translator.translate(text, 'ja', 'en').text)	