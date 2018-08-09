from docxExtractor import extract_docx_text
from pdfExtractor import extract_pdf_text
import sys
import codecs
from textUtility import word_similarity

def main(file1, file2):

	sentences_file1 = extractText(file1)
	sentences_file2 = extractText(file2)
	generateReport(sentences_file1, sentences_file2, 0.7)

		

def extractText(file):
	sentences = []
	if file.endswith('.docx'):
		sentences = extract_docx_text(file)
	elif file.endswith('.pdf'):
		sentences = extract_pdf_text(file)
	else:
		raise ValueError('Unsupported File Extension!')
	
	return sentences
	
	
def generateReport(sentence_list1, sentence_list2, threshold):
	f = codecs.open("report.txt", "w", "utf-8")
	sameCount = 0
	for i in range(0, len(sentence_list1)):
		for j in range(0, len(sentence_list2)):
			if word_similarity(sentence_list1[i].upper(), sentence_list2[j].upper())>threshold:
				sameCount = sameCount + 1
				f.write("--------SENTENCES WITH SIMILARITY OF " + str(word_similarity(sentence_list1[i].upper(), sentence_list2[j].upper())) + " -----\n\n")
				f.write(sentence_list1[i]+"\n\n\n")
				f.write("     AND     \n\n\n")
				f.write(sentence_list2[j]+"\n\n\n")
				f.write("--------------------------------------------------------\n\n\n\n")
	f.close()
	print("NUMBER OF SIMILAR SENTENCES: " + str(sameCount))


if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2])