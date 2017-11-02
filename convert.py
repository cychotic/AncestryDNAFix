import sys

try:
    filename = sys.argv[1]
except IndexError:
    filename = "AncestryDNA.txt"

ancestry = open(filename, 'r')

template = open("template.txt",'r')
fixed = open("fixed_"+filename, 'w')

lookup = {}
templatecount = 0
filecount = 0
writecount = 0
replacecount = 0
skipcount = 0

for line in ancestry:
    if "#" in line:
        fixed.write(line)
        writecount += 1
    else:
        lookup[line.split('\t')[0]] = line
    filecount += 1

for line in template:
    if "#" in line:
        pass
    else:
        try:
            fixed.write(lookup[line.split('\t')[0]])
            replacecount += 1
        except KeyError:
            fixed.write(line)
            skipcount += 1
        writecount += 1
    templatecount += 1

ancestry.close()
template.close()
fixed.close()

print("template lines: "+str(templatecount))
print("file lines: "+str(filecount))
print("new lines: "+str(writecount))
print("replaced lines: "+str(replacecount))
print("skipped lines: "+str(skipcount))