# FASTQ to FASTA
!pip install Bio
from Bio import SeqIO

"""
NOTE: Be sure to upload a fastq file. If you have a txt file, you can easily convert it into fastq format by changing the name of the file. No conversions between file types necessary, just 
change the file type. (e.g. rename data.txt to data.fastq). Once you have changed the format, upload your saved fastq file.
"""
fastq_file = input("What is the name of your fastq file? ")


"""
NOTE: Create an empty txt file in a text editor and then convert the txt file to a fasta file type using the same method as above. Just rename the empty file. Once you have changed file format, upload 
your saved fasta file to your desired coding platform.
"""
fasta_file = input("What is the name of your desired fasta file? ")

# opens the fastq file, opens a writable blank fasta, SeqIO parses fastq and uses SeqIO to write it to a fasta file
with open(fastq_file) as input_handle, open(fasta_name, 'w') as output_handle:
    my_fq = SeqIO.parse(input_handle, "fastq")
    SeqIO.write(my_fq, output_handle, 'fasta')
