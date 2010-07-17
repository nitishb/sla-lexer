import sys
from itextextractor import *

if __name__ == "__main__":
	if len(sys.argv) == 2:
		file = sys.argv[1]
		f = open(file,"r")
		print "TOKEN STREAM"
		while(True):
			token = gettoken(f)
			if token[0] == 'EOF':
				break
			print token
		f.close()
