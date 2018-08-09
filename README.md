# Document Comparator

Python project that compares two documents for similar sentences. Documents can be of either .docx or .pdf format.


## Prerequisites

Project was written using Python 3.7. It uses additional python modules:
	
	* pdfminer
	* docx
	
Once you download the project, before running it, make sure you update pip from command line like so:

```
python -m pip install --upgrade pip
```

When update is complete run from command line:

```
pip install -r requirements.txt
```

inside the project directory to install all the necessary modules. Once that is done you are ready to go!

## Running the project

When running from command line, make sure documents to be compared are located in the project directory. Then just run something like:

```
python compareDocuments.py [NAME_OF_FIRST_FILE_TO_BE_COMAPRED] [NAME_OF_SECOND_FILE_TO_BE_COMAPRED]
```

in the command line. After some time, you will be prompted with a message that looks like:

```
NUMBER OF SIMILAR SENTENCES: 156
```

And then it is done! You can review similar sentences and their level of similarity in the generated report.txt file.

Note: Comparison can take up to several minutes. Extracting text from .pdf files also takes some time...


## Further Improvements

-Other algorithms to find out similarity between sentences. For example cosine similarity.

-Allowing other file extensions to be comparable.

-Finding similarity between sentences that seem different due to synonyms being used.
