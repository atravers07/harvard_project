#!/usr/bin/env python3

import re						#for regular expressions
from collections import Counter	#to use counter() function
import json						#to use json file


def main():

	my_dic = {}					#dictionnary creation
	words = re.findall('\w+', open('text.txt').read().lower())	#to find words without punctuation, in small letters
	my_dic = Counter(words)		#to put counter dictionnary in my_dic
	for k in my_dic.keys():		#to have each word's frequency
		my_dic[k]/= len(words)
	#print(my_dic)
	with open('destination.json','w') as fp:	
		json.dump(my_dic, fp)


if __name__ == "__main__":
    main()

