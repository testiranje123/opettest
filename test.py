import ruamel.yaml

import requests
import json

import xml.dom.minidom as MD

class User():
	def __init__(self):
		self.id=None
	def __str__(self):
		return "jovanic"

	def print(self):
		print(self.age)

def mul(a,b):
	return a*b

print(mul(4,2))


with open("user.yaml","r") as stream:
	f=ruamel.yaml.safe_load(stream)

print(f)
user=User()
user.age=56

print(user.print())
print(user)
for i in f[0]["martin"]:
	print (i)



userd=user.__dict__
print (json.dumps(userd, indent=4))

dom=MD.parse("user.xml")

#print(dir(dom.getElementsByTagName("ime").item(0).childNodes.item(0)))
#print(dom.getElementsByTagName("ime").item(0).childNodes.item(0).wholeText)

breakfast=dom.childNodes[0]
print (breakfast)
print (breakfast.nodeName)

ime=breakfast.childNodes[1]

print(ime)
print(ime.nodeName)

print(ime.childNodes[0])
print(ime.childNodes[0].nodeValue)

print("u test ")

print("a sada ga ja menjam")

o=3
u=6
d=o+u
print(d)
print("neko drugi je menjao nesto")
a=1
b=9
c=a+b
print(c)

#root=dom.childNodes
#print (root)
#for nodes in root.item(0).childNodes:
#	print("wtf", nodes)
#	if nodes.childNodes.item(0):
#		print(nodes.childNodes.item(0))
