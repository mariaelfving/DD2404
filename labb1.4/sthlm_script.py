# Code

file = open('sthlm.txt','r')
lines = file.readlines()

output=''

n=0
file = open('sthlm.txt','r')
for i in range(0,len(lines)):
    line = file.readline()
    if line.startswith('#'):
        pass
    elif line.startswith('/'):
        pass
    else:
        n+=1
        output=output+line.split(' ')[0]+'\n'

print(str(n))
print(output)


# Explain the general structure of a Stockholm file. What is an "accession"?
## Always begins with # STOCKHOLM <version>
## Can have markers #=GF, #=GS, #=GR and #=GC that gives information
## Other lines contain: <seqname> \tab <aligned sequence>
## Accession numbers are unique identifiers
