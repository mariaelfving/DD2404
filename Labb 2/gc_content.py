import sys
import fileinput

def read_file(file_in):
    seq = ''
    for line in file_in:
        if line[0] == '>':
            pass
        else:
            seq = seq + line
    return seq

def count_nuc(seq):
    gc = 0
    at = 0
    for i in range(0,len(seq)):
        if seq[i] == 'C' or seq[i] == 'G':
            gc += 1
        else:
            at += 1
    gc_cont = float(gc) / float(gc+at)
    return gc_cont

if __name__ == '__main__':
    for name in sys.argv[1:]:
        file_in = open(str(name),'r')
        seq = read_file(file_in)
        gc_cont = count_nuc(seq)
        print('%.3f' % gc_cont)

# python gc_content.py bacill.txt chlam.txt haemo.txt legion.txt thermo.txt

# Why do people care about GC content?
