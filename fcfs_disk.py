import math
size=int(input("enter no. of tracks"))
t=[]
for i in range(size):
    t.append(int(input("enter track no. {0}\n".format(i+1))))
head=int(input("enter the head position: \n"))
current=head
seek=t[0]-head
for i in range(size-1):
     seek=seek+abs(t[i]-t[i+1])
print(seek)
    
