#!/usr/bin/bash
#File:generate_directories.sh

#################
# This script will create several new files with gene* nomenclature
# in a new directory named sequences/


#################


directories=(
geneA_01.fn
geneA_02.fn
geneA_03.fasta
geneA_04.fn
geneB_01.fn
geneB_02.fn
geneC_01.fn
geneC_02.fasta
geneC_03.fn
geneC_04.fn
geneD_01.fn
geneD_02.fasta
geneE_01.fn
geneF_01.fn
)

mkdir sequences

for file in ${directories[@]};do
	touch sequences/$file
done