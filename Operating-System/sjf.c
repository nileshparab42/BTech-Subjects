#include<stdio.h>
int main()
{
    int n, i, bt[20], pid[20], wt[20], tat[20], tot_tat, tot_wt, j, temp;
    float  avg_tat, avg_wt;
    printf("Enter number of process : \n");
    scanf("%d", &n);
    printf("\n");
    printf("Enter the brust time : \n");
    for(i=1;i<=n;i++)
    {
        printf("p%d : ",i);
        scanf("%d",&bt[i]);
        pid[i]=i;
    }
    printf("\n");
    for(i=1;i<=n;i++)
    {
        for(j=1;j<n;j++)
        {
            if(bt[j]>bt[j+1])
            {
                temp=bt[j];
                bt[j]=bt[j+1];
                bt[j+1]=temp;

                temp=pid[j];
                pid[j]=pid[j+1];
                pid[j+1]=temp;
            }
        }
    }
    wt[1]=0;
    for(i=2;i<=n;i++)
        {
            wt[i]=wt[i-1]+bt[i-1];            
        }

    for(i=1;i<=n;i++)
        {
            tat[i]=wt[i]+bt[i];            
        }

    tot_tat=0;
    for(i=1;i<=n;i++)
        {
            tot_tat=tat[i]+tot_tat;           
        }
    avg_tat=tot_tat/n;

    tot_wt=0;
    for(i=1;i<=n;i++)
        {
            tot_wt=wt[i]+tot_wt;           
        }
    avg_wt=tot_wt/n;

    printf("Analysis Table :\n");
    printf("pid : bt : wt : tat \n");
    for(i=1;i<=n;i++)
        {
            printf(" p%d :  %d :  %d :  %d \n",pid[i],bt[i],wt[i],tat[i]);
        }
    printf("\n");
    printf("Averages :\n");
    printf("Average Weating time : %f\n",avg_wt);
    printf("Average Turnaround time : %f\n",avg_tat);

    printf("\n");
    printf("Grantt chart :\n");
    printf(":");
    for(i=1;i<=n;i++)
        {
            printf(" p%d :",pid[i]);
        }
    printf("\n");

    return 0;
}