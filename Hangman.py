from random import choice


class Hangman:
    """ Implementation of the word game Hangman in Python """
    def __init__(self, word):
        self.actual = word
        self.word = word[:-1]
        self.errors = 0
        self.length = len(self.word)
        self.display = '-' * self.length
        self.already_guessed = []

    # Drawing of gallows (The hanged man) present in file 'gallows.txt'
    def get_gallows(self, mistakes):
        f2 = open('gallows.txt')
        content = f2.read()
        f2.close()
        gallows = content.split('#')
        for i in gallows:
            if len(i) == 0:
                gallows.remove(i)
        return gallows[mistakes]

    def play(self):

        print(self.get_gallows(self.errors))
        print('The Word: ', self.display)

        guessed = input('\nGuess a letter: ').lower()

        # If player tries to guess the whole word
        if len(guessed) > 1:
            if guessed == self.actual[:-1]:
                print("\nWOW! You did it! the word was in fact ", self.actual)
                return 1
            else:
                self.errors += 1
                print(self.get_gallows(self.errors))
                if self.errors == 7:
                    print('You have failed to guess the word. It was', self.actual)
                    return
                else:
                    print('WRONG! Try again...'.format(guessed))
                    self.play()

        # If the input is empty or is a number
        elif len(guessed) == 0 or guessed.isnumeric():
            print('Invalid input. Try entering a letter: ')
            self.play()

        # If the input is repeated
        elif guessed in self.already_guessed:
            print('You\'ve already tried that one before. Try another: ')
            self.play()

        # If the input is a match
        elif guessed in self.word:
            self.already_guessed.append(guessed)
            for index in range(len(self.word)):
                if self.word[index] == guessed:
                    self.word = self.word[:index] + '-' + self.word[index + 1:]
                    self.display = self.display[:index] + guessed + self.display[index + 1:]

            if self.word == '-' * self.length:
                print('\nWOOP WOOP... Congrats!!!\nThe word was indeed', self.actual)
                return 1
            else:
                self.play()

        # If the input doesn't match any letters in our chosen word
        else:
            self.errors += 1
            self.already_guessed.append(guessed)
            print(self.get_gallows(self.errors))
            if self.errors == 7:
                print('You have failed to guess the word. It was', self.actual)
                return
            else:
                print('WRONG! Try again...'.format(guessed))
                self.play()


# The word will get randomly chosen from 834 words in 'word.txt'
def get_word():
    f1 = open('words.txt')
    word_list = f1.readlines()
    f1.close()
    word = choice(word_list)
    return word


player1 = Hangman(get_word())
print('\n----    Welcome to Hangman    ----')
player1.play()
