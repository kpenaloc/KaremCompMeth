#HW 1 for Computational Methods 
import sys
import string, argparse
import numpy as np
# from astropy import units as u

def time_to_drop(height, grav):
		time = np.sqrt(2*height/grav)
		return time


def main():  
	parser = argparse.ArgumentParser()
	parser.add_argument('h', help="The height of the ball above the ground, in meters", type=float)

	parser.add_argument('-g', help="The acceleration due to gravity on your planet, in meters per seconds-square", type=float, default=9.8)

	args = parser.parse_args()
	h = args.h
	g = args.g


	print("This program will compute how long it will take for an object to drop from a specified height.")

	print("Your ball is ", h, "meters above the ground. The acceleration due to gravity is ", g, "meters per seconds-square.")

	# graveyard of ideas for more-than-the-minimum

	# if(grav==9.8): 
	# 	print("You are on Earth")

	# else:
	# 	print("you are not on Earth")

	## cool to have unit parser that takes in a string and splits # from unit

	time = time_to_drop(h, g)

	print("It will take your object ", time, "seconds to drop to the ground.")

if __name__ == '__main__':
    main()