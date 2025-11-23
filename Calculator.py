#!/usr/bin/env python3
"""Basic menu-driven calculator.

Supports: addition, subtraction, multiplication, division, power, percentage.
This is intentionally simple and uses plain float arithmetic.
"""

import sys


def get_number(prompt):
	while True:
		try:
			return float(input(prompt))
		except ValueError:
			print('Please enter a valid number.')


def add():
	a = get_number('First number: ')
	b = get_number('Second number: ')
	print(f'Result: {a + b}')


def subtract():
	a = get_number('Minuend: ')
	b = get_number('Subtrahend: ')
	print(f'Result: {a - b}')


def multiply():
	a = get_number('First number: ')
	b = get_number('Second number: ')
	print(f'Result: {a * b}')


def divide():
	a = get_number('Dividend: ')
	b = get_number('Divisor: ')
	if b == 0:
		print('Error: division by zero')
		return
	print(f'Result: {a / b}')


def power():
	a = get_number('Base: ')
	b = get_number('Exponent: ')
	print(f'Result: {a ** b}')


def percent():
	value = get_number('Value: ')
	pct = get_number('Percent (e.g. enter 20 for 20%): ')
	print(f'Result: {value * (pct / 100.0)}')


def menu():
	print('Basic Calculator')
	print('1) Add')
	print('2) Subtract')
	print('3) Multiply')
	print('4) Divide')
	print('5) Power')
	print('6) Percent')
	print('0) Exit')


def main():
	while True:
		menu()
		choice = input('Choose an option: ').strip()
		if choice == '1':
			add()
		elif choice == '2':
			subtract()
		elif choice == '3':
			multiply()
		elif choice == '4':
			divide()
		elif choice == '5':
			power()
		elif choice == '6':
			percent()
		elif choice == '0' or choice.lower() in ('q', 'quit', 'exit'):
			print('Goodbye')
			return
		else:
			print('Unknown option. Please choose 0-6.')


if __name__ == '__main__':
	try:
		main()
	except (KeyboardInterrupt, EOFError):
		print('\nGoodbye')
		sys.exit(0)

