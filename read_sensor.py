from time import sleep


count =0
while True:
	f=open('example.txt','r').read()
	lines = f.split('\n')
	for line in lines:
		sleep(1)
		print(count , line)
		count +=1
	
