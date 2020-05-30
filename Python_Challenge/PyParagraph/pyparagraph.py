import re
import csv
import os
fileList = ["paragraph_1.txt","paragraph_2.txt"]
for file in fileList:
    txtpath = os.path.join("Pyparagraph",file)
    with open(txtpath, 'r') as text:   
        lines = text.read()
        sentences = re.split(r'(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?)\s', lines)
        words = re.split(r' ', lines)                    
        letterCount = 0
        for word in words:
            letterCount = letterCount + len(word)
        outputpath = os.path.join("paragraph_1.txt",file.split(".")[0] + "_result.txt")

        lines = []
    
        resultsfile = open(outputpath, "w")
    
        lines.append("Paragraph Analysis")
        lines.append("-----------------")
        lines.append("Approximate Word Count:: "+str(len(words)))
        lines.append("Approximate Sentence Count: "+str(len(sentences)))
        lines.append("Average letter count: "+ str(round(letterCount/len(words),2)))
        lines.append("Average Sentence Length: "+ str(round(len(words)/len(sentences),2)))
        for line in lines:
            print(line)
            print(line,file=resultsfile)
        print()
        resultsfile.close()