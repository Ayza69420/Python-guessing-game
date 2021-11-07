from time import time
from random import randint
from colorama import Fore as FORE, Style as STYLE
from os import system

class main:
    def __init__(self, mode=1):
        '''
        # Modes
        1 = Easy\n
        2 = Medium\n
        3 = Hard\n
        Default value being equal to easy.
        '''

        try:
            assert(mode == 1 or mode == 2 or mode == 3)
        except AssertionError:
            print('Mode must be 1 (Easy) or 2 (Medium) or 3 (Hard).')
            exit()


        self.mode = mode
        self.guessed = False
        self.time_taken = time()
        self.guesses = 0
        self.hard_maximum_guesses = 5
        self.hard_maximum_hints = 1
        self.last_guessed_number = None
        self.hints = 0
        self.maximum_hints = 5
        self.msg = ''
        self.number = self.generate_random_number()


    def won(self):
        system('cls')
        
        print(f'{FORE.GREEN}{STYLE.BRIGHT}You got the number {self.number} right!{FORE.RESET}')
        print(f'Amount of guesses taken: {FORE.RED if self.guesses > 10 else FORE.GREEN}{STYLE.BRIGHT}{self.guesses}{FORE.RESET}')
        print(f'Time taken: {FORE.RED if round(int(time()-self.time_taken)) >= 60 else FORE.GREEN}{STYLE.BRIGHT}{round(int(time()-self.time_taken))}{FORE.RESET} seconds')
        self.guessed = True

    def lost(self):
        if not self.guessed:
            print(f'{FORE.RED}{STYLE.BRIGHT}Sorry! You lost for taking more than {self.hard_maximum_guesses} tries. The number was {self.number}.{FORE.RESET}')

    def generate_random_number(self): 
        if self.mode == 1: # easy
            return randint(1,15)
        elif self.mode == 2: # medium
            return randint(50,150)
        elif self.mode == 3: # hard
            return randint(100,500)

    def display_mode(self):
        if self.mode == 1:
            return f'{FORE.GREEN}{STYLE.BRIGHT}Mode: Easy{FORE.RESET}'
        elif self.mode == 2:
            return f'{FORE.YELLOW}{STYLE.BRIGHT}Mode: Medium{FORE.RESET}'
        elif self.mode == 3:
            return f'{FORE.RED}{STYLE.BRIGHT}Mode: Hard (Meaning you can only take 1 hint now. Good luck!){FORE.RESET}'


    def start(self):
            while not self.guessed and (self.guesses < self.hard_maximum_guesses if self.mode == 3 else 999999999999999):
                try:
                    system('cls')
                    
                    print(self.display_mode())
                    print(self.msg)

                    guessed_number = input('Guess a number:\n')

                    if guessed_number.isalpha():
                        if guessed_number.lower() == 'hint':
                            if self.last_guessed_number != None and self.hints < (self.maximum_hints if self.mode != 3 else self.hard_maximum_hints):

                                if self.last_guessed_number < self.number:
                                    self.msg = ('Too low')
                                    self.hints += 1
                                    continue
                                elif self.last_guessed_number > self.number:
                                    self.msg = ('Too high')
                                    self.hints += 1
                                    continue
                                    
                            elif self.mode == 3:
                                self.msg = (f'{FORE.RED}{STYLE.BRIGHT}You cannot take more than {self.hard_maximum_hints} hints.{STYLE.BRIGHT}{FORE.RESET}')
                                continue                                
                            elif self.mode != 3:
                                self.msg = (f'{FORE.RED}{STYLE.BRIGHT}You cannot take more than {self.maximum_hints} hints.{STYLE.BRIGHT}{FORE.RESET}')
                                continue

                            else:
                                self.msg = ('You must make a first guess.')
                                continue   

                            
                    else:
                        self.last_guessed_number = int(guessed_number)
                        self.guesses += 1

                        if int(guessed_number) == self.number:
                            self.won()
                        else:
                            self.msg = ('Wrong.')
                            continue
                except ValueError:
                    print('You must input an integer.')
            self.lost()


game = main() # Takes one argument, the mode which is set to 1 (Easy) as default.

game.start()
