#include<iostream>
using namespace std;
void first_fit(int processno,int blockno,int *process,int *block)
{
    int allocation[processno];
    for(int i=0;i<processno;i++)
    {
        allocation[i]=-1;
    }
    for(int i=0;i<processno;i++)
    {
        for(int j=0;j<blockno;j++)
        {
            if(block[j]>=process[i])
            {
                allocation[i]=j;
                block[allocation[i]]-=process[i];
                break;
            }
        }
    }
   cout<<"process no.  "<<"           "<<"process size."<<"                      "<<"block no. "<<endl;
   for(int k=0;k<processno;k++)
   {
        cout<<k+1<<"                            "<<process[k]<<"                     ";
        if(allocation[k]==-1)
        {
          cout<<"Not Enough Space"<<endl;
        }
        else
        {
            cout<<allocation[k]+1<<endl;
        }

   }
}
int main()
{
    int blockno,processno;
    cout<<" ENTER THE NUMBER OF MEMORY BLOCKS :"<<endl;
    cin>>blockno;
    cout<<"ENTER THE NUMBER OF PROCESSES: "<<endl;
    cin>>processno;
    cout<<endl;
    int b[blockno],p[processno];
    cout<<"ENTER THE SIZE OF EACH BLOCK: "<<endl;
    for (int  i = 0; i < blockno; i++)
    {
        cin>>b[i];
    }
    cout<<endl<<"ENTER THE SIZE OF EACH PROCESS: "<<endl;
    for (int  i = 0; i < processno; i++)
    {
        cin>>p[i];
    }
    first_fit(processno,blockno,p,b);

}