#everyone is fucking stupid

import random

class insultgen():
	def __init__(self):
		self.beginning = ['You have got to be kidding me, you', 'You must be a', 'You are a', 'Ah, you are a typical']
		self.adjective = ['dirty', 'grimy', 'chinese', 'lousy', 'skanky', 'brainless', 'dumb', 'lackluster', 'fascinating', 'supreme', 'master']
		self.noun = ['chinaman', 'chinawoman', 'skank', 'trollop', 'cretin', 'degenerate',
		'darwin award 2015 winner', 'bimbo', 'donkey', 'git', 'wanker', 'sausage jockey',
		'rick ross', 'dummmy']
		self.end = ['Kill yourself.', 'I love you.', 'Never talk to me again.']


	def generateInsult(self):
		x = random.randint(0, len(self.beginning) - 1)
		y = random.randint(0, len(self.adjective) - 1)
		z = random.randint(0, len(self.noun) - 1)
		sidjizz = random.randint(0, len(self.end) - 1)

		insult = self.beginning[x] + " " + self.adjective[y] + " " + self.noun[z] + ". " + self.end[sidjizz]

		return insult

if __name__ == '__main__':
   swag = insultgen()
   print swag.generateInsult()