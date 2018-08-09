import docx
from textUtility import cleanUpText

def extract_docx_text(file):
	#extract text from document
	doc1 = docx.Document(file)
	extractedText = []
	for para in doc1.paragraphs:
		extractedText.append(para.text)
	
	returnText = cleanUpText(extractedText)
	
	return returnText
