def myfind(indir):
	import os 
	out = os.listdir(indir)
	files = []
	for file in out: 
		if ".txt" in file: 
			files.append(open(indir+"\\"+file))	
	newfiles = []		
	for file,i in zip(files,range(len(files))): 
		newfiles.append([])
		for line in file: 
			newfiles[-1].append(line)
			
	while True: 
		query = raw_input()
		for file,filetitle in zip(newfiles,out): 
			for line in file: 
				if query in line: 
					print filetitle,":::",line
					
