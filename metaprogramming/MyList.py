# Metaprograming/MyList.py
def howdy(self, you):
    print "Howdy, " + you

MyList = type('MyList', (list, ), dict(x=42, howdy=howdy))

myList = MyList()
myList.append("Camembert")
print myList
print myList.x
myList.howdy("Uyen")


print(myList.__class__.__class__)