import random

'list of the words->'
word_bank  = ['rizz', "ohio","sigma","tiktok","skibidi","restrain","element","fiction","custody","powder","gravity","review","suppress","joy","reinforce","requirement","strain","shine","final","mud"]

'random selection of word'
word = random.choice(word_bank)
guessed_word = ['_']*len(word)
attempts = 10

'''Game Loop'''

while attempts>0:
    print('\nCurrent Word '+' '.join(guessed_word))

    guess = input('Guess a letter: ')

    if guess in word:
        for i in range(len(word)):
            if word[i] == guess:
                guessed_word[i] = guess
        print('Great guess!')
    else:
        attempts-=1
        print('wrong guess! Attempts left: '+str(attempts))
    if '_' not in guessed_word:
        print('\nCongratulation!! You guessed the word: '+word)
        break