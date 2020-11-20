import json

filename = "positive-words.txt"

lofwords = []

with open(filename) as pw:
    for line in pw:
        pword = line.strip().split(None)
        
        lofwords.append(pword)

out_file = open("positive-words.json", "w")
json.dump(lofwords, out_file, sort_keys=False)
out_file.close