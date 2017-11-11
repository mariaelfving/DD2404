from random import randint

length = input('How long should the sequence be? ')

nuc_list = ['A','C','T','G']
nuc_seq = ''

for i in range(0,int(length)):
    random = randint(0,len(nuc_list)-1)
    nuc = nuc_list[random]
    nuc_seq = nuc_seq + nuc;

print('>random_sequence \n' + nuc_seq)
