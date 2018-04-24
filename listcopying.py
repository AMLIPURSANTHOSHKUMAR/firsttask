import copy
a=[10,20,[30,40,50],70,80,90]
print(a)
b=a
print("changes done to a")
a[0]=5
print(a,"\n",b)
print("\n\n\n")
a=[10,20,[30,40,50],70,80,90]
b=a
print("changes done to b")
b[0]=6
print(a,"\n",b)
print("\n\n\n")
a=[10,20,[30,40,50],70,80,90]
print("copying a list to b and changing the value of 30")
b=copy.copy(a)
a[2][0]=3
print(a,"\n",b)
print("\n\n\n")
a=[10,20,[30,40,50],70,80,90]
print(a)
print("changes occurs to only a")
b=copy.deepcopy(a)
a[2][1]=4
print(a,"\n",b)
print("\n\n\n")
a=[10,20,[30,40,50],70,80,90]
print(a)
print("changes done to only a ")
b=copy.copy(a)
a[3]=7
print(a,"\n",b)
print("\n\n\n")
a=[10,20,[30,40,50],70,80,90]
print(a)
b=copy.deepcopy(a)
a[4]=8
print(a,"\n",b)
print("\n\n\n")
a=[10,20,[30,40,50],70,80,90]
print(a)
b=a
print("extending the a list and verifing b list")
a.extend([100,110,120,130])
print(a,"\n",b)
print("\n\n\n")
a=[10,20,[30,40,50],70,80,90]
print(a)
print("extending the b list and verifying the a list")
b=a
b.extend([100,110,120,130,140,150])
print(a,"\n",b)
print("\n\n\n")
a=[10,20,[30,40,50],70,80,90]
print("extending the b list it does not change the a list")
print(a)
b=copy.deepcopy(a)
b.extend([111,222,333,444,555])
print(a,"\n",b)


