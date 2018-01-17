import random
import urllib2


class Game(object):

    response = urllib2.urlopen("http://svnweb.freebsd.org/csrg/share/dict/words?view=co&content-type=text/plain")
    dictionary = response.read().splitlines()
    word = ''
    scenes = {0: '______ \n|   | \n|   \n| \n|   \n| \n========',
              1: '______ \n|   | \n|   O \n| \n|   \n| \n========',
              2: '______ \n|   | \n|   O \n|   | \n|   \n| \n========',
              3: '______ \n|   | \n|   O \n|  /| \n|   \n| \n========',
              4: '______ \n|   | \n|   O \n|  /|\\ \n|   \n| \n========',
              5: '______ \n|   | \n|   O \n|  /|\\ \n|  /  \n| \n========',
              6: '______ \n|   | \n|   O \n|  /|\\ \n|  / \\ \n| \n========',
              }

    def __init__(self):
        print '\nWELCOME TO HANGMAN'
        print '------------------'

    def play(self):
        self.word = random.choice(self.dictionary).lower()
        won = False
        wrong = 0
        previous = ''
        current = '_' * len(self.word)
        while not won:
            print self.scenes[wrong]
            if wrong > 5:
                print "Game over."
                print 'The word was', self.word
                break
            print current, '\n'
            print "Letters guessed:", previous
            letter = raw_input('Guess letter: ')
            if len(letter) != 1:
                'Please enter one letter at a time.'
            elif letter in previous:
                print 'Letter already guessed - try again!'
            elif letter in self.word:
                print 'Yay \n'
                previous = previous + letter
                copy = self.word
                count = 0
                while letter in copy:
                    index = copy.index(letter) + count
                    copy = copy[:(index - count)] + copy[(index - count + 1):]
                    current = current[:index] + letter + current[(index + 1):]
                    count += 1
                if current == self.word:
                    print 'Winner!'
                    print 'The word was', self.word
                    won = True
            else:
                print 'Nope \n'
                wrong += 1
                previous = previous + letter


if __name__ == '__main__':
    game = Game()
    game.play()
    done = False
    while not done:
        again = raw_input("Would you like to play again? (y/n) ")
        if again == 'y':
            print "Okay, a new word has been selected. \n"
            game.play()
        elif again == 'n':
            done = True
        else:
            print "Enter either 'y' or 'n'"
    print 'Thanks for playing!'
