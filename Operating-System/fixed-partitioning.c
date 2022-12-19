#include<stdio.h>
#include<conio.h>
int main()
{
    int m,npt,nps,s,pos,i,mps[10],frac,tfrac;
    printf("Enter memory size :\n");
    scanf("%d",&m);
    printf("Enter number of partitions :\n");
    scanf("%d",&npt);
    s=m/npt;
    pos=m;
    printf("Size of individual partition is %d\n",s);
    printf("Enter no of processes :\n");
    scanf("%d",&nps);
    for(i=0;i<nps;i++)
    {
        
        if(pos<s)
        {
            printf("There is no further memory left for the process %d\n",i+1);
            mps[i]=0;
            break;
        }
        else
        {
            printf("Enter memory size of process %d :\n",i+1);
            scanf("%d",&mps[i]);
            if(mps[i]<s)
            {
                printf("Process %d is allocated in memory\n",i+1);
                frac=s-mps[i];
                printf("Internal fragmentation for process %d is %d\n",i+1,frac);
                tfrac=tfrac+frac;
                pos=pos-s;
            }
            else
            {
                printf("Process %d is not allocated in the memory\n",i+1);
            }
        }
    }
    printf("Total fragmentation : %d\n",tfrac);
    getch();
    return 0;
}