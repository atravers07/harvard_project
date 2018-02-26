#!/usr/bin/env python3

def main():
	#f=open("text.txt","r")
	my_dictionnary={}
	ponctuation_list=[",","?",";",".",":","/","!","'","(",")","[","]"]
	with open('text.txt','r') as my_file:
		contenu=my_file.read()
		print(contenu)
	for char in ponctuation_list:
		contenu2=my_file.replace(char,' ')
		print(contenu2)
	#f=f.lover()
	#	for line in my_file:
	#		words=line.split()
		for word in contenu:
			if word in my_dictionnary:
				my_dictionnary[word]+=1
			else:
				my_dictionnary[word]=1	
		for cle in my_dictionnary:
			print(cle)
	

if __name__=="__main__":
	main()

