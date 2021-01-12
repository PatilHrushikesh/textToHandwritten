#
from PIL import Image
from countwordlen import imgwidth
#import pytesseract
import random
import string
import os

width,height = 715,760
arr= 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789+,.-?:/*<>}{()=[]$" '
# arr = string.ascii_letters
# arr = arr + string.digits + "+,.-?:/*<>}{()= "
imgsource="myfont\\"
pageheight=7624
pagewidth=5940
start=715
end=5930
pageno=0
print(arr)

# back=none
def getpage():
	global back,pageno
	try:
		pageno+=1
		bg = Image.open("myfont\\backpage.png", 'r')
		back = Image.new('RGBA', (5952,8088), (0, 0, 0, 0))
		back.paste(bg, (0,0))
		# addroll() # This function is to add rollnumber at the top margin of page
		print("OUT")
	except:
		print("backpage not found")
		exit() 

def savepage():
	path="final\\done"

	i=1
	while os.path.exists(path+str(i)+".png"):
		i+=1;
	back.save(path+str(i)+".png","PNG")
	print("Saved done"+str(i)+".png .......n")


def pasteimg(case,start,height):
	global back
	# print(width,height)
	try:
		cases = Image.open(imgsource+"%s.png"%case)
		back.paste(cases,(start,height),mask=cases)
		start = start + cases.width + random.randint(5,15) 
	except:
		print(case+" Case not found")
	return start

def getname(letter):
	#IF you are adding new letter add it in arr also (line around 10)
	if letter.isupper():
		letter = "c"+letter.lower()
	elif letter == ",":
		letter = "coma"
	elif letter == ".":
		letter = "fs"
	elif letter == "?":
		letter = "que"
	elif letter == "<":
		letter = "ang1"
	elif letter == ">":
		letter = "ang2"
	elif letter == "{":
		letter = "cur1"
	elif letter == "}":
		letter = "cur2"
	elif letter == ":":
		letter = "colon"
	elif letter == "/":
		letter = "div"
	elif letter == "-":
		letter="sub"
	elif letter == "(":
	    letter = "par1"
	elif letter == ")":
	    letter = "par2"
	elif letter == "[":
	    letter = "sqr1"
	elif letter == "]":
	    letter = "sqr2"
	elif letter == "*":
	    letter = "star"
	elif letter == "=":
	    letter = "equal"
	elif letter == "+":
	    letter = "plus"
	elif letter == "$":
	    letter = "dol"+str((random.randint(1,2)))
	elif letter == '"':
	    letter = "quo"
	
	
	#IF you are adding new letter add it in arr also (line around 10)
	return letter

def getwordpix(word):
	wordwid=0
	for char in word:
		if char in arr:
			img=getname(char)
			wordwid+=imgwidth[img]
	return wordwid

def getnewline(start,cur,end,height):
	global back
	height = height + 244
	if height>pageheight:
		getnewpage()
		return start,760
	else:
		start=720+(random.randint(0,100))
		# print("   NEWLINE :",height);
	return start,height

def getnewpage():
	savepage()
	getpage()

def formatting(word,leng,start,cur,ecfnd):
	global height
	if leng>=2:
		if word[:2]=="^^":
			word=word[2:]
			cur+=(2418-int(getwordpix(word)/2))
		if word[:2]=="->":
			word=word[2:]
			cur+=400
	return word,cur
def maketable(content,height,start,cur,end):
	# print(content)
	columns=int(content[0])
	ratio=[]
	total=0
	i=0
	for C in range(0,columns):
		i+=1
		print(content[i])
		total+=int(content[i])
		ratio.append(int(content[i]))
	prev=i+1
	base=5237/total
	content=" ".join(content[i+1:])
	print(content)
	try:
		row=content.split("#");
		print("----")
		for R in row:
			col=R.split("|")
			colno=0
			for C in col:
				print("!!!!")
				print(C)
				start,cur,end,height=condition(height, base*colno+width, base*colno+width, base*(colno+1)+width-20, content)

	except Exception as e:
		print("Error in Maketable height",height)
		print(e)

def checktag(content,i,height,start,cur,end):
	print("NEW ",content[i])
	if content[i]=="<table>":
		
		try:
			print("Making table....")
			index=content.index("</table>",i+1)
			content=content[i+1:index]
			print(content)
			cols=int(content[0])
			total=0
			ratio=[0]
			for j in range(1,cols+1):
				print(j,"-> ",content[j])
				total+=int(content[j])
				ratio.append(int(content[j]))
			base = (end-start)/total
			content = content[cols+1:index]
			content= " ".join(content)
			print(content)
			row = content.split("#")
			maxheight=0
			i=0
			lastheight=height
			for R in row:
				for C in R.split("|"):
					C= C.split()
					start, cur, end, height1 = condition(
						lastheight, start+base*ratio[i], start+base*ratio[i], start+base*ratio[i+1], C)
					if(height1>maxheight):
						maxheight=height1
				lastheight=maxheight
				i+=1
			# maketable(content[i+1:indesx],height,start,cur,end)
			return index+1
		except Exception as e:
			print(e)
			print("     </table> not found")
			exit()
	return 0

# def addroll():
# 	global arr,back
# 	print("Addding rollno")
# 	wid,hei=4000+(random.randint(-400,200)),300+(random.randint(-100,200))
# 	# wid, hei =4200, 500
# 	getno=random.randint(1,3)
# 	roll = "roll"+str(getno)
# 	pasteimg(roll, wid, hei)
# 	print("REtuning")

	
def condition(height,start,cur,end,content):
	print("IN condition\n\n\n")
	global arr,back
	first=1
	count=0
	for i in range(0,len(content)):
		word=content[i]
		print(word)
		ind=checktag(content,i,height,start,cur,end)
		# return 0
		if ind:
			i=ind
			continue
		print("This word  :",word," <-")
		halfword=0
		leng=len(word)
		wordwid=0
		word,cur=formatting(word,leng,start,cur,end)
		wordwid=getwordpix(word)

		widthafterpaste=cur+wordwid+70
		print(wordwid)
		print("width+wordwid=",cur+wordwid,"  Page width=",end)

		cur+=60+random.randint(0,35)
		if widthafterpaste > end:#If current word width is greater 
											#than available
			diff=widthafterpaste-end
			if(leng>5 and diff>((0.4*leng)+250)):
				print("Half word can be fit")
				halfword=1
			else:

				print("--------Word does not Fit-------")
				print(cur,"  ",height)
				cur,height=getnewline(start,cur,end,height)
				print(cur,"  ",height)

		if height>3500 and first:
			height+=10
			first=0
		for letter in word:
			# print(letter+"    ",end="");
			if letter == "#":
				cur,height=getnewline(start,cur,end,height)
				continue
			if letter in arr:        
				letter=getname(letter)

				if halfword and cur + random.randint(200,280) >= end:
					# pasteimg("sub")
					print("Half word.....",end)
					cur,height=getnewline(start,cur,end,height)
					# pasteimg("sub")
				print(cur,height)   
				cur=pasteimg(letter,cur,height)
	# sleep(100)
	return start,cur,end,height
    # back.close()
        
def readfile():
    pass

def extract():
	try:
		filepath="MyText.txt"
		file = open(filepath, encoding="utf8")
		content=file.read()
		file.close()
		print(content)
		content=content.split()
		getpage()
		condition(height,start,start,end,content)
		savepage()

    
	except Exception as e:
		print(e)

extract()
