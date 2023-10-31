# fastq-to-fasta
Converts a file from a FASTQ to FASTA format. FASTA and FASTQ are two very common file formats for bioinformatics and DNA analysis. FASTA shows a tag that identifies one of the "short-reads" in a genetic sample, and then depict the corresponding genetic sequence. However, FASTQ shows the tag, then the sequence, and then adds a string full of symbols that represent the Phred Quality score of the read. Phred Quality represents how accurate a read is. Q30 means a 99.9% accuracy, Q40 means a 99.99% accuracy rate. Q30 and Q40 are the most common Phred Quality scores.
Created in Python 3.
October 31st, 2023 by Sanat Rao
MIT License
