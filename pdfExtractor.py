import io
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfpage import PDFPage
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from textUtility import cleanUpText

def extract_pdf_text(file):

	# set up PDF miner
	rsrcmgr = PDFResourceManager()
	sio = io.StringIO()
	codec = 'utf-8'
	laparams = LAParams()
	device = TextConverter(rsrcmgr, sio, codec=codec, laparams=laparams)
	interpreter = PDFPageInterpreter(rsrcmgr, device)

    # get pages from pdf
	fp = open(file, 'rb')
	for page in PDFPage.get_pages(fp):
		interpreter.process_page(page)
	fp.close()

    # Get text from StringIO
	extractedText = sio.getvalue()

    # Cleanup
	device.close()
	sio.close()
	
	returnText = cleanUpText(extractedText)

	return returnText