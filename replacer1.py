import re

file = open('RepInput.txt', 'r')
lines = file.readlines()

for line in lines:
    outfile = open('RepOut.txt', 'a')
    processed = re.sub('the ', "cum ", line)
    pro2 = re.sub("The ", "cum ", processed)
    outfile.write(pro2)
    outfile.close()
file.close()
