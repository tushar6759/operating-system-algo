def waiting_time(l,num):
    start_time=0  
    wt_list=[0]
    for i in range(1,num+1):
        start_time=start_time+l[i-1][2]   # start time += burst time of i-1 process
        if l[i][0]>start_time:
            start_time=l[i][0]
            wt_list.append(0)
        else:
            wt=start_time-l[i][0]         #wt=start_time - arrival time of current process
            if wt<0:
                wt=0
            wt_list.append(wt)
    return wt_list


def turnaround_time(wait,l,num):
    tat=[0]
    for i in range(1,num+1):
        t=wait[i]+l[i][2]      #t=wait+burst_time
        tat.append(t)
    return tat
    

def average_time(l,num):
    
   wait=waiting_time(l,num)
   avg_wait=sum(wait)/num
   tat=turnaround_time(wait,l,num)
   avg_tat=sum(tat)/num
   print('process  arrival time   burst time    turnaround time     waiting time')
   for i in range(1,num+1):
       print('{}              {}               {}                {}                 {}'.format(l[i][1],l[i][0],l[i][2],tat[i],wait[i]))
   print('AVERAGE TURNAROUND TIME IS : ',avg_tat)
   print('AVERAGE WAITING TIME IS : ',avg_wait)
    


n=int(input('Enter the number of processes: '))
# [[arrival time, process id , burst time]]
p=[[0,0,0]]
for i in range(1,n+1):
    a=int(input('ENTER THE ARRIVAL TIME OF %d:'%i))
    b=int(input('ENTER THE BURST TIME OF %d:'%i))
    p.append([a,i,b])
p.sort()
average_time(p,n)
    


    
    
