#!/usr/bin/env python3

def main():
	f=open("text.txt","r")
	my_dictionnary={}
	ponctuation_list=[",","?",";",".",":","/","!","'","(",")","[","]"]
	for char in ponctuation_list:
		f=f.replace(char,' ')
	f=f.lover()
	for line in f:
		words=line.split()
		for word in words:
			if word in my_dictionnary:
				my_dictionnary[word]+=1
			else:
				my_dictionnary[word]=1	
	for cle in my_dictionnary:
		print(cle)
	

if __name__=="__main__":
	main()
