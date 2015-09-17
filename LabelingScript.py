def StartLabeling(inputfile,positivefile,negativefile,processedfile,startline): 
	input = open(inputfile)
	positive = open(positivefile,"a")
	negative = open(negativefile,"a")
	processed = open(processedfile,"a")
	pcount = 0
	ncount = 0 
	for line in input:
		if(startline>0): 
			startline-=1
			continue
		print line
		x = raw_input()
		if x=='0':
			ncount+=1
			print "Shortcut",pcount
			print "None",ncount
			negative.write(line)
			negative.flush()
		elif x=='1': 
			pcount+=1
			print "Shortcut",pcount
			print "None",ncount
			positive.write(line)
			positive.flush()
		processed.write(line)
		processed.flush()
	positive.close()
	negative.close()
	processed.close()
		

		
		
StartLabeling(r'C:\NLP Files\Shortcuts.txt',r'C:\NLP Files\PositiveShortcuts.txt',r'C:\NLP Files\None.txt',r'C:\NLP Files\Processed.txt',0)