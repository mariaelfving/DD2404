# Code

import math

def generate_fasta(line):
    fasta = '>'+line.split(' ')[0].split('\t')[0]+'\n'+line.split(' ')[len(line.split(' '))-1].split('\t')[len(line.split('\t'))-1]
    return fasta

def fix_lines(fasta):
    line = fasta.split('\n')[1]
    if len(line) > 60:
        fasta_output = fasta.split('\n')[0]+'\n'
        for j in range(0,int(math.ceil(len(line)/60))):
            fasta_output = fasta_output+line[j*60:j*60+59]+'\n'
    else:
        fasta_output = fasta
    return fasta_output

filename = input('What file do you wanna open? ')

file = open(str(filename),'r')
lines = file.readlines()

output=''
file = open(str(filename),'r')
for i in range(0,len(lines)):
    line = file.readline()
    if line.startswith('#'):
        pass
    elif line.startswith('/'):
        pass
    else:
        if len(line)<2:
            pass
        else:
            fasta = generate_fasta(line)
            fasta_output = fix_lines(fasta)
            output=output+fasta_output
print(output)

# What is Pfam?
## Pfam is a database of protein families that includes their annotations and
## multiple sequence alignments.
