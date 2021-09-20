#arrival time 0
def average_turn_wait(b,n1):
    tat=[0]
    wt=[0]
    ct=0
    for i in range(1,n1+1):
          ct=ct+b[i]
          tat.append(ct)
          wt.append(tat[i]-b[i])

    print('process  arrival time   burst time    turnaround time     waiting time')
    for i in range(1,n1+1):
          print('{}              {}               {}                {}                 {}'.format(i,0,b[i],tat[i],wt[i]))
    print("\n average turn around time is : ",sum(tat)/n1)
    print("average waitting time is : ",sum(wt)/n1)
    
n=int(input('enter the no. of processes:'))
d=[0]
for i in range(1,n+1):
    d.append(int(input('burst time of %d : '%i)))
average_turn_wait(d,n)
