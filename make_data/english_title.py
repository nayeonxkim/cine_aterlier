import googletrans
translator = googletrans.Translator()
temp = 'Il buono, il bruto, il cattivo'
temp2 = '헌 트'
out_temp = translator.translate(temp, dest='en', src='auto')
print(out_temp)
# print(temp.isalpha())
# print(temp2.isalpha())

# 띄어쓰기, a~z아니면 다 아님.
def is_english(sentence):
    pass

