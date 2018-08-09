from difflib import SequenceMatcher

def cyrillicDecode(text):
	#list of all the lowercase letters
	cyrillicLowercase = ['а','б','в','г','д','ђ','е','ж','з','и','ј','к','л','љ','м','н','њ','о','п','р','с','т','ћ','у','ф','х','ц','ч','џ','ш']
	latinLowercase = ['a','b','v','g','d','đ','e','ž','z','i','j','k','l','lj','m','n','nj','o','p','r','s','t','ć','u','f','h','c','č','dž','š']

	#creating lists of uppercase letters from the lowercase ones
	cyrillicUppercase = []
	latinUppercase = []

	for i in range(0,len(cyrillicLowercase)):
		cyrillicUppercase.append(cyrillicLowercase[i].title())

	for i in range(0,len(latinLowercase)):
		latinUppercase.append(latinLowercase[i].title())
	
	
	#replacing the cyrillic alphabet with a latin one
	for i in range(0,len(cyrillicLowercase)):
		text = text.replace(cyrillicLowercase[i], latinLowercase[i])
	
	for i in range(0,len(cyrillicUppercase)):
		text = text.replace(cyrillicUppercase[i], latinUppercase[i])

	return text
	
	
def removeShortSentences(sentenceList):
	sentenceList = list(filter(None, sentenceList))
	removeSentences = []
	for i in range(0, len(sentenceList)):
		if (len(sentenceList[i])<30):
			removeSentences.append(sentenceList[i])
	for i in range(0, len(removeSentences)):
		sentenceList.remove(removeSentences[i])
	return sentenceList
	
	
def cleanUpText(sentenceList):
	sentences = []
	if(isinstance(sentenceList,str)):
		sentenceList = cyrillicDecode(sentenceList)
		tempSent = sentenceList.split(".")
		for j in range(0, len(tempSent)):
			sentences.append(tempSent[j])
	else:
		for i in range(0,len(sentenceList)):
			sentenceList[i] = cyrillicDecode(sentenceList[i])
		sentenceList = list(filter(None, sentenceList))
		for i in range(0, len(sentenceList)):
			tempSent = sentenceList[i].split(".")
			for j in range(0, len(tempSent)):
				sentences.append(tempSent[j])
	
	returnText = removeShortSentences(sentences)
	
	return returnText
	
def word_similarity(a, b):
    return SequenceMatcher(None, a, b).ratio()
	
