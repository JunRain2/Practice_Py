#윈도우에서 파일을 열 때 tkinter의 파일 열기 대화상자를 통해 쉽게 찾을 수 있다.
from tkinter import *
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import asksaveasfilename

readFile = askopenfilename()
if (readFile != None):
    infile = open(readFile, "r")
    
for line in infile.readlines():
    line = line.strip()
    print(line)
    
infile.close()
