
# Adds a record to a file
def add(arr, path):
	filea = open(path, "a+")
	for item in arr:
		filea.write(str(item)+"; ")
	filea.write("\n")

# Searches for records  in a file
# Returns a list of strings as result 
def search(num, path, returnAll=1):
	filer = open(path, "r+")
	res = []
	with filer as f:
		lines = f.read()
		line = lines.split("\n")
		for l in line:
			words = l.split("; ")
			curid = words[0]
			if (curid==""):
				break
			if (words[0]==num):
				res.append(l)
				if (returnAll==0):
					break
	return res
