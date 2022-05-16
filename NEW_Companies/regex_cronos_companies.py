from cmath import e
import re

file = open('./companies_raw/staatsbladmonitor.txt', 'r')

list_companies = []

for line in file:
    line = line.strip()
    r = re.findall(r'(label: \'\w+\')|(label: \'\w+ \w+\')|(label: \'\w+ \w+ \w+\')|(label: \'\w+ \w+ \w+ \w+\')', line)
    string_r = ''.join(map(str,r)).strip()

    labels = re.findall(r'(?s)(?<=label: \').*?(?=\'\")', str(string_r))
    string_labels = ''.join(map(str,labels))
    
    list_companies.append(string_labels)

with open('companies_staatsblad.txt', 'w') as f:
    for item in list_companies:
        f.write(item + '\n')