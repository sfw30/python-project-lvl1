#!/usr/bin/env python
from brain_games.logic.welcome import welcome_text
from brain_games.cli import hello_user
from brain_games.logic.constants import NAME
from brain_games.scripts.brain_even import even_check


def main():
    welcome_text()
    hello_user()
    even_check()


if __name__ == '__main__':
	main()

