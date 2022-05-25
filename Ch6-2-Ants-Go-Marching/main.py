def ant(number, action):
	print("The ants go marching", number, "by", number,",","hurrah, hurrah")
	print("The ants go marching", number, "by", number+",","hurrah, hurrah")
	print("The ants go marching", number, "by", number+",")
	print("The little one stops to", action)
	print("And they all go marching down...\nTo the ground...\nTo get out of the rain. BOOM! BOOM! BOOM!")


def main():
	number=["one","two","three","four","five","six","seven","eight","nine","ten"]
	action=["say I'm done","take a poo","then go pee","kill a boar","taunt the bee hive","lay some bricks","pin on a chevron","act as bait","drink some wine","draw Big Ben"]

	for i in range(len(number)):
		ant(number[i],action[i])
		print(), print()


main()