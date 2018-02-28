#!/usr/bin/env python3
#coding=utf-8

#for regular expressions
import re		
#to use json file
import json
#to use argparse
import argparse
#to use counter() function				
from collections import Counter						

#creation of arguments
parser = argparse.ArgumentParser(description='Process some integers')
parser.add_argument('--fileToRead', help="name of the input file")
parser.add_argument('--resultFile', help="name of the output file")
parser.add_argument('inputDir')
parser.add_argument('outputDir')
args = parser.parse_args()
if args.fileToRead:
	input_file=args.fileToRead
if args.resultFile:
	result_file=args.resultFile
input_dir = args.inputDir
output_dir = args.outputDir

def main(in_file, out_file, in_dir, out_dir):
	
	#dictionnary creation
	my_dic = {}
	#to find words without punctuation, in small letters					
	words = re.findall('\w+', open(in_dir+"/"+in_file).read().lower())
	#to put counter dictionnary in my_dic	
	my_dic = Counter(words)	
	#to have each word's frequency	
	for k in my_dic.keys():		
		my_dic[k]/= len(words)
	#to put my_dic in a JSON file and returning to the next line at every new key
	with open(out_dir+"/"+out_file,'w') as fp:	
		json.dump(my_dic, fp,indent=2)


if __name__ == "__main__":
    main(input_file, result_file, input_dir, output_dir)

