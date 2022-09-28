# encoding: utf-8


import sys
from Bio import Seq
from Bio import SeqIO





input = sys.argv[1]
with open(input, "r") as input_handle:
	for record in SeqIO.parse(input_handle, "genbank"):
		print()
		#print(record)
		#print(record.seq) # The sequence itself, typically a Seq object
		#print(record.id) #The primary ID used to identify the sequence – a string(Acc number)
		#print(record.name) #A “common” name/id for the sequence
		#print(record.description) #A human readable description or expressive name for the sequence – a string
		#print(record.letter_annotations) #Holds per-letter-annotations using a dictionary of additional information about the letters in the sequence
		#print(record.dbxrefs)  #A list of database cross-references as string (Bioproject,Biosample,Assembly)
		#print(record.features)

	
	#feature object	
	for feature in record.features:
		#print feature
		#print feature.type # Description of the type of feature (for instance,‘CDS’ or ‘gene’)
		
		#location attribute
		#print feature.location 
		#print feature.location.start
		#print feature.location.end
		#print feature.location.strand

		#qualifiers attribute
		#print feature.qualifiers #This is a Python dictionary of additional information about the feature

		if feature.type == 'CDS':
			#print (">"+feature.qualifiers['locus_tag'][0])
		 	# try:
		 	# 	print (feature.qualifiers['gene'][0])
	 		# except:
	 	 	# 	print "NA" 
		 	# try:
		 	# 	print feature.qualifiers['EC_number'][0]
		 	# except:
		 	# 	print "NA"

		 	#print feature.qualifiers['product'][0]
		 	#print feature.qualifiers['translation'][0]

		 	#print feature.location.start
			#print feature.location.end
			#print feature.location.strand
			#print "\n"



			#how to extract DNA position (Be careful with strand)
			start = feature.location.start
			end = feature.location.end
			strand = feature.location.strand
			
			#print strand
			#print record.seq[start:end]
			



			#how to extract DNA position (Be careful with strand)
		
			if strand < 0:
				sequence =  record.seq[start:end]
				

				locus = feature.qualifiers['locus_tag'][0]
				print(">"+locus+"\n"+sequence.reverse_complement()+"\n")
			else:
				sequence =  record.seq[start:end]
				#print sequence

				locus = feature.qualifiers['locus_tag'][0]
				print(">"+locus+"\n"+sequence+"\n")









