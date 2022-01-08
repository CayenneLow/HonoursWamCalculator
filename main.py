import re
import PyPDF2

sumMarkUocWeighting = 0
sumUocWeighting = 0
totUoc = 0

def processText(text):
    global sumMarkUocWeighting, sumUocWeighting, totUoc
    regex = "(\w{4}) (\d)\d{3}(.+?)\d.00 (\d.00)(1*\d\d)*(EC|SY|PS|CR|DN|HD)"
    matches = re.findall(regex, text)
    for match in matches:
        courseCode = match[0]
        if courseCode == "GENC":
            weight = 1
        else:
            if int(match[1]) > 4:
                weight = 4
            else:
                weight = int(match[1])
        uoc = float(match[3])
        totUoc += uoc
        if match[4] != '':
            mark = int(match[4])
            sumMarkUocWeighting += (mark * uoc * weight)
            sumUocWeighting += (uoc * weight)
 
pdfFileObj = open('transcript.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

markObj = {}
 
nPages = pdfReader.numPages
i = 0
while i < nPages:
    pageObj = pdfReader.getPage(i)
    text = pageObj.extractText()
    processText(text)
    i += 1

#print(f"{sumMarkUocWeighting} / {sumUocWeighting} = {sumMarkUocWeighting/sumUocWeighting}")
honoursWam = sumMarkUocWeighting/sumUocWeighting
print(f"Honours Wam: {honoursWam} ({totUoc} UOC)")
if (honoursWam >= 80):
    print("Congratulations, you've made First Class Honours")
    
 
pdfFileObj.close()