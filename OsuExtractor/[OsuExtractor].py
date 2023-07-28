import zipfile
import os
import sys
import math

sepMap = "§"
sepCat = "µ"
sepKey = "¨"
sepVal = ";"
enc = 'utf-8'

def sortDouble(a,b):
	r = []
	while len(b)>0:
		be = False
		bi = 0
		i = 0
		for x in b:
			if not be or x<be:
				be = x
				bi = i
			i+=1
		if be:
			r.append(a[bi])
			b.pop(bi)
			a.pop(bi)
	return r
def Decrypt(FileName):
	with zipfile.ZipFile(FileName,"r") as zip:
		print(" Converting "+FileName)
		n = FileName[:-4].split(" - ")
		author = n[0]
		title = n[1]
		n = zip.namelist()
		files = []
		maps = []
		for name in n:
			if name[-3:] == "osu":
				files.append(zip.extract(name))
		contents = []
		dif = []
		for file in files:
			with open(file,"r",encoding=enc) as file_in:
				txt = ""
				obj = []
				State = "Start"
				meta = {}
				for line in file_in:
					line = line[:-1]
					if line != "" or line != "\n" or line != "\r\n":
						if State == "[HitObjects]":
							obj.append(line)
						elif State == "[Metadata]"or State == "[Difficulty]" or State == "[General]":
							s = line.split(":")
							if len(s)>1:
								k = s[0]
								meta[k] = s[1]
								if k=="OverallDifficulty":
									dif.append(s[1])
						if line == "[HitObjects]"or line == "[General]"or line == "[Metadata]"or line == "[Difficulty]"or line == "[Events]"or line == "[TimingPoints]"or line == "[Colours]":
							State = line
				txt = txt+sepMap
				metaSort = {}
				sortList = ["Title","Artist","Creator","Version","Mode","OverallDifficulty","AudioLeadIn","PreviewTime"]
				for k in sortList:
					metaSort[k] = meta[k]
				for k in metaSort:
					v = metaSort[k]
					txt = txt+k+sepKey+v+sepVal
				txt = txt+sepCat
				for line in obj:
					e = line.split(",")
					x,y,time,ty = e[0],e[1],e[2],e[3]
					txt = txt+x+","+y+","+time+","+ty+";"
				contents.append(txt)
			os.remove(file)
		with open(title+".txt","w",encoding=enc) as f:
			master = sortDouble(contents,dif)
			f.write("".join(master))

if len(sys.argv)>1:
	i = 0
	for file in sys.argv:
		if i>0:
			Decrypt(file)
		i+=1
		if len(sys.argv)>2:
			os.system("cls")
			print(" Converting "+str(len(sys.argv)-1)+" files. ("+str(i-1)+"/"+str(len(sys.argv)-1)+")")
			l = ""
			for x in range(i-1):
				l = l+"#"
			for x in range(len(sys.argv)-i):
				l = l+"-"
			print(" Loading ["+l+"]")
else:
	exist = False
	print('[Tip]: You can drag an .osz file over the python script')
	while not exist:
		zipname = input("Enter .osz file : ")+".osz"
		exist = os.path.exists(zipname)
		if not exist:
			os.system("cls")
			print(" This file doesn't exist.")
	os.system("cls")
	Decrypt(zipname)
l = 50
txt = "Done"
line = " "
for x in range(l):
	line = line+"_"
line = line+"\n\n "
txtI = 0
for x in range(l-len(txt)):
	if x>=(l-len(txt))*.5 and x<(l+len(txt))*.5:
		line = line+txt[txtI]
		txtI+=1
	else:
		line = line+" "
line = line+"\n "
for x in range(l):
	line = line+"_"
print(line+"\n",end="\n ")
#os.system("pause")