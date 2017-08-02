import os
from textblob.classifiers import NaiveBayesClassifier
#a
def featurevector(word1,asc):
	l=len(asc)+1
	#print (l)
	fv=[0]*l
	for word in word1:
		if word in asc:
			for i in range(0,len(asc)):
				fv[asc.index(word)]=1
		
	return (fv)
def testfv(word1,asc):
	l=len(asc)
	#print(l)
	fv=[0]*l
	for word in word1:
		if word in asc:
			fv[asc.index(word)]=1
			
	return (fv)
	
wc=[]
wc1=[]
f=open("C:/Users/patel_000/Documents/data mining/Assignment/a5/Assignment5/stoplist.txt")
sl=[]
sl=[word for line in f for word in line.split()]
def arxiv():
	#a
	for root, dirs, files in os.walk("C:/Users/patel_000/Documents/data mining/Assignment/a5/Assignment5/articles/arxiv"):
		for f in files:
			wc=[line.split() for line in open(os.path.join(root, f), "r")]
			wc1=[word for line in open(os.path.join(root, f), "r") for word in line.split() if word.lower() not in sl]
	training,testing=wc1[0:24],wc1[25:50]
	#print (training)
	#print(testing)
	#print (sl)
	asc=sorted(training)
	train1=[]
	for word1 in wc:
		train1.append(featurevector(word1,asc))
	p1=[]	
	for line in train1:
		q=map(str,line)
		p1.append([''.join(q),"a"])
		#p1.extend(["a"])
	#print (p1)

	test=[]
	for word1 in wc:
		test.append(testfv(word1,testing))
	p=[]	
	for line in test:
		q=map(str,line)
		p.append(''.join(q))

	#print (p)
	return p1,p
#a=[training.append(["a"])]
#print(a)

def jdm():
	#j
	for root, dirs, files in os.walk("C:/Users/patel_000/Documents/data mining/Assignment/a5/Assignment5/articles/jdm"):
		for f in files:
			wc=[line.split() for line in open(os.path.join(root, f), "r")]
			wc1=[word for line in open(os.path.join(root, f), "r") for word in line.split() if word.lower() not in sl]
	training1,testing1=wc1[0:24],wc1[25:50]
	asc=sorted(training1)
	train1=[]
	for word1 in wc:
		train1.append(featurevector(word1,asc))
	p11=[]	
	for line in train1:
		q=map(str,line)
		p11.append([''.join(q),"j"])
		#p1.extend(["a"])


	test=[]
	for word1 in wc:
		test.append(testfv(word1,testing1))
	p2=[]	
	for line in test:
		q=map(str,line)
		p2.append(''.join(q))
	return p11,p2
	
def plos():
	#p
	for root, dirs, files in os.walk("C:/Users/patel_000/Documents/data mining/Assignment/a5/Assignment5/articles/plos"):
		for f in files:
			wc=[line.split() for line in open(os.path.join(root, f), "r")]
			wc1=[word for line in open(os.path.join(root, f), "r") for word in line.split() if word.lower() not in sl]
	training2,testing2=wc1[0:24],wc1[25:50]
	asc=sorted(training2)
	train1=[]
	for word1 in wc:
		train1.append(featurevector(word1,asc))
	p111=[]	
	for line in train1:
		q=map(str,line)
		p111.append([''.join(q),"p"])
		#p1.extend(["a"])


	test=[]
	for word1 in wc:
		test.append(testfv(word1,testing2))
	p3=[]	
	for line in test:
		q=map(str,line)
		p3.append(''.join(q))
	return p111,p3
#-----------
p1,p=arxiv()
p11,p2=jdm()
p111,p3=plos()
new1=[]
new2=[]

#print(p1)
cl=NaiveBayesClassifier(p1)
new=[]
for line in p:
	new.append([line,cl.classify(line)])	
for line in p2:
	new1.append([line,cl.classify(line)])
#print(new)
for line in p3:
	new2.append([line,cl.classify(line)])
accuracy=cl.accuracy(p1+new)
print('Accuracy for arxiv:%i'% accuracy)
accuracy=cl.accuracy(p11+new1)
print('Accuracy for jdm:%i'% accuracy)
accuracy=cl.accuracy(p111+new2)
print('Accuracy for plos:%i'% accuracy)
new.extend(new1)
new.extend(new2)
#print(new)
p1.extend(p11)
p1.extend(p111)
print('------------------')
for i in p1:
	for j in new:
		if i[0] ==j[0] :
			if i[1]=='a' and j[1]=='a':
				print('Actual class: arxiv')
				print('Classified Class:arxiv')
				print('-------------------------')
			if i[1]=='a' and j[1]=='j':
				print('Actual class: arxiv')
				print('Classified Class:jdm')
				print('-------------------------')
			if i[1]=='a' and j[1]=='p':
				print('Actual class: arxiv')
				print('Classified Class:plos')
				print('-------------------------')
			if i[1]=='j' and j[1]=='a':
				print('Actual class: jdm')
				print('Classified Class:arxiv')
				print('-------------------------')
			if i[1]=='j' and j[1]=='j':
				print('Actual class: jdm')
				print('Classified Class:jdm')
				print('-------------------------')
			if i[1]=='j' and j[1]=='p':
				print('Actual class: jdm')
				print('Classified Class:plos')
				print('-------------------------')
			if i[1]=='p' and j[1]=='a':
				print('Actual class: plos')
				print('Classified Class:arxiv')
				print('-------------------------')
			if i[1]=='p' and j[1]=='j':
				print('Actual class: plos')
				print('Classified Class:jdm')
				print('-------------------------')
			if i[1]=='p' and j[1]=='p':
				print('Actual class: plos')
				print('Classified Class:plos')
				print('-------------------------')

