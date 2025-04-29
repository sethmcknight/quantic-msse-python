print('Welcome to Cactus World!\nTell us a few words that\nremind you of cacti!\n')

#  Get 4 words associated with cacti from the user
cactus_associated_words = []
for i in range(4):
    word = input('Enter a word associated with cacti: ')
    cactus_associated_words.append(word)
# Print the words
print(f'The words you entered are: {cactus_associated_words}')