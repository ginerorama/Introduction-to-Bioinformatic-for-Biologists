# encoding: utf-8


import sys
from Bio import Seq
from Bio import SeqIO
import pandas as pd 


#SeqIO.read() for fasta

input = sys.argv[1]
with open(input, "rU") as input_handle:
	for record in SeqIO.parse(input_handle, "fasta"):
		print(record)
		#print(record.seq) # The sequence itself, typically a Seq object
		#print(record.id) #The primary ID used to identify the sequence – a string(Acc number)
		#print(record.name) #A “common” name/id for the sequence
		#print(record.description) #A human readable description or expressive name for the sequence – a string
		#print(record.letter_annotations) #Holds per-letter-annotations using a dictionary of additional information about the letters in the sequence
		#print(record.dbxrefs)  #A list of database cross-references as string (Bioproject,Biosample,Assembly)
		#print(record.features)