#!/usr/bin/python3

from generator import *
import sys

def main(dest, classes_path):
	data = ClassData(classes_path)
	gen = Generator(data)
	gen.output(dest)

if __name__ == "__main__":
	if len(sys.argv) < 3:
		print("  Usage: gen.py <dest> <classes_data>")
		exit()

	directory = sys.argv[1]
	classes_path = sys.argv[2]

	main(directory, classes_path)









