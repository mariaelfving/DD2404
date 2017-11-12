import math
import pdb

def generate_newgroup(file):
    new_group=[]
    for i in range(0,len(lines)):
        line = file.readline()
        if line.startswith('>'):
            new_group.append(i)
        else:
            pass
    new_group.append(len(lines))
    return new_group

def generate_sequence(new_group,lines,j):
    seq=''
    for k in range(new_group[j]+1,new_group[j+1]):
        seq=seq+lines[k][:-1]
    return seq

def generate_string(section,string,str_list):
    for m in range(0,int(math.floor(len(section)/3+1))):
        part = section[3*m:3*m+3]
        if len(part)<3:
            break
        if part=='TGA' or part=='TAG' or part=='TAA' or part=='tga' or part=='tag' or part=='taa':
            str_list.append(string)
            string=''
        else:
            string=string+part
    return string

def generate_strlist(seq,string):
    for l in range(0,3):
        section = seq[l:].split('\n')[0]
        if len(section)<3:
            string=''
            str_list.append(string)
            break
        string = generate_string(section,string,str_list)
        str_list.append(string)
        string=''
    return str_list

def generate_amino(longest,dict_amino):
    amino=''
    for n in range(0,int(math.floor(len(longest)/3))):
        codeon = longest[3*n:3*n+3]
        codeon = codeon.upper()
        if 'A' in codeon or 'T' in codeon or 'C' in codeon or 'G' in codeon:
            amino=amino+dict_amino[codeon]
        else:
            amino=amino+'X'
    return amino

dict_amino = {'GCT':'A', 'GCC':'A', 'GCA':'A','GCG':'A', 'CGT':'R', 'CGC':'R',
    'CGA':'R', 'CGG':'R', 'AGA':'R', 'AGG':'R', 'AAT':'N', 'AAC':'N', 'GAT':'D',
    'GAC':'D', 'TGT':'C', 'TGC':'C', 'CAA':'Q', 'CAG':'Q', 'GAA':'E', 'GAG':'E',
    'GGT':'G', 'GGC':'G', 'GGA':'G', 'GGG':'G', 'CAT':'H', 'CAC':'H', 'ATT':'I',
    'ATC':'I', 'ATA':'I', 'TTA':'L', 'TTG':'L', 'CTT':'L', 'CTC':'L', 'CTA':'L',
    'CTG':'L', 'AAA':'K', 'AAG':'K', 'ATG':'M', 'TTT':'F', 'TTC':'F', 'CCT':'P',
    'CCC':'P', 'CCA':'P', 'CCG':'P', 'TCT':'S', 'TCC':'S', 'TCA':'S', 'TCG':'S',
    'AGT':'S', 'AGC':'S', 'ACT':'T', 'ACC':'T', 'ACA':'T', 'ACG':'T', 'TGG':'W',
    'TAT':'Y','TAC':'Y', 'GTT':'V', 'GTC':'V', 'GTA':'V', 'GTG':'V'}

# Code
filename = input('What file do you wanna open? ')
file = open(str(filename),'r')
lines = file.readlines()
output=''
file = open(str(filename),'r')
new_group = generate_newgroup(file)

for j in range(0,len(new_group)-1):
    str_list = []
    #pdb.set_trace()
    output = output+lines[new_group[j]].split(' ')[0].split('\n')[0]+'\n'
    string = ''
    seq = generate_sequence(new_group,lines,j)
    str_list = generate_strlist(seq,string)
    if not str_list:
        pass
    else:
        longest = max(str_list,key=len)
        longest = longest.split('\n')[0]
        #pdb.set_trace()
        amino = generate_amino(longest,dict_amino)
        output = output+amino+'\n'

print(output)

#How did you structure your code and why?

#What are the "stop codons" in the standard code?
## TGA, TAG and TAA

#Why are we talking about a "standard code"?
## We have non-standard amino acids and variations, giving other results
## and stop codons

#Looking for the longest ORF is a primitive way to find genes in prokaryotic genomes.
#Why does it not work for eukaryotes?
## The main problem with the genomes of higher eukaryotes in general is that
## their genes are often split by introns, and so do not appear as continuous
## ORFs in the DNA sequence

#What is the longest protein snippet produced on the file an_exon.fa?
## 111

#Why should a real ORF finder also look at the so-called Watson-Crick complement?
## Watson Crick complement is a string representing the complementary
## DNA strand (T <-> A, G <-> C). Need to look at this as well to get whole helix
