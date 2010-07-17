# 				***		Lexical Analyzer for XML Files.		***
#
#
#  Given an sla document (sla is the file format of Scribus, which is XML), extract all the text contents (Embedded using ITEXT tag) removing all tags and #  save it as a text file.
#
#  SLA file format specification : http://wiki.scribus.net/index.php/File_Format_Specification_for_Scribus_1.4
#
#  Programming Language : Python
#
#  Group Members: 
#
#    * #2  - Alex Poovathingal
#    * #19 - Jain Basil Aliyas
#    * #61 - Vinu Vincent
#	

import sys

# Returns the next valid token from the file pointer f

def gettoken(f):
	c = f.read(1)
	while(c.isspace()):
		c = f.read(1)
	if c == '':
		return ['EOF']
	elif c == '<':
		c = f.read(1)
		if c == '/' or c == '?':
			return ["START"]
		else:
			f.seek(-1,1)
			return ["START"]
	elif c.isalpha():
		buf = ""
		while(True):
			buf = buf + c
			c = f.read(1)
			if c == '>' or c == '/' or c == '?':
				f.seek(-1,1)
				return ["TAGNAME", buf]
			if c.isspace():
				return ["TAGNAME", buf]
			elif c == "=":
				return ["ATTRNAME", buf]
	elif c == '\"':
		buf = ""
		while(True):
			c = f.read(1)
			if c == '\"':
				return ["STRING", buf]
			buf = buf + c
	elif c == '/' or c == '?':
		c = f.read(1)
		if c == ">":
			return ["END"]
	elif c == ">":
		return ["END"]	
	else:
		print "Lex Error at " + str(f.tell()) + "position"	# Error Report


# Extracts text contents from the file

def itextextractor(filename):
	f = open(filename,"r")
	w = open("output","w")
	while(True):
		token = gettoken(f)
		if token[0] == "EOF":
			break
		if token[0] == "START":
			while(True):			
				token = gettoken(f)	
				if token[0] == "TAGNAME":
					if token[1] == "ITEXT":
						while(True):
							token = gettoken(f)
							if token[0] == "ATTRNAME":
								if token[1] == "CH":
									token = gettoken(f)
									if token[0] == "STRING":
										w.write(token[1])
										print token[1]
									else:
										break
							elif token[0] == "END" or token[0] == 'EOF':
								break;
				elif token[0] == "END" or token[0] == 'EOF':
					break;
	w.close()
	f.close()
	

if __name__ == "__main__":
	if len(sys.argv) == 2:
		file = sys.argv[1]
		itextextractor(file)
