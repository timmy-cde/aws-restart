import re

# open file
textFile = open("preproinsulin-seq.txt", "r")

# filter string
sequence = textFile.read()
chars = ['O', 'R', 'I', 'G', 'N', '1', '6', ' ', '/', '\n']
pattern = '[' + ''.join(chars) + ']'
modSequence = re.sub(pattern, '', sequence)

# check output and length
print(modSequence)
print(len(modSequence))

# write to new file
newSeq = open("preproinsulin-seq-clean.txt", "w")
newSeq.write(modSequence)

# close files
textFile.close()
newSeq.close()


# open the filtered file
cleanSeq = open("preproinsulin-seq-clean.txt", "r")

# initialize strings
lsinsulin = ""
binsulin = ""
cinsulin = ""
ainsulin = ""

# loop characters
for char in cleanSeq:
    
    # lsinsulin-seq-clean.txt 1-24 (24 char)
    for i in range(0, 24):
        lsinsulin += char[i]
    
    # binsulin-seq-clean.txt 25-54 (30 char)
    for i in range(24, 54):
        binsulin += char[i]
    
    # cinsulin-seq-clean.txt 55-89 (35 char)
    for i in range(54, 89):
        cinsulin += char[i]
    
    # ainsulin-seq-clean.txt 90-110 (21 char)
    for i in range(89, 110):
        ainsulin += char[i]

# validate ouput
print(lsinsulin)
print(len(lsinsulin))

print(binsulin)
print(len(binsulin))

print(cinsulin)
print(len(cinsulin))

print(ainsulin)
print(len(ainsulin))

ls = open("lsinsulin-seq-clean.txt", "w")
b = open("binsulin-seq-clean.txt", "w")
c = open("cinsulin-seq-clean.txt", "w")
a = open("ainsulin-seq-clean.txt", "w")

# write to file
ls.write(lsinsulin)
b.write(binsulin)
c.write(cinsulin)
a.write(ainsulin)

# close files
cleanSeq.close()
ls.close()
b.close()
c.close()
a.close()