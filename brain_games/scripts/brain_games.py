#!/usr/bin/env python

from brain_games.cli import welcome_user

def greet(welcome):
    print('{}'.format(welcome))

def main():
    greet('Welcome to the Brain Games!')
    welcome_user()

if __name__ == '__main__':
    main()
