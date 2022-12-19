#include<stdio.h>
#include<conio.h>
int main()
{
    int bno,bsize[10],pno,psize[10],flag[10],allocation[10],i,j;

    for(i=0;i<10;i++)
        {
            flag[i]=0;
            allocation[i]=-1;
        }

    printf("Enter number of blocks :\n");
    scanf("%d",&bno);
    printf("Enter size of blocks : \n");
    for(i=0;i<bno;i++)
        {
            printf("b[%d]",i);
            scanf("%d",&bsize[i]);
        }

    printf("Enter number of processes :\n");
    scanf("%d",&pno);
    printf("Enter size of processes : \n");
    for(i=0;i<pno;i++)
        {
            printf("b[%d]",i);
            scanf("%d",&psize[i]);
        }
    
    for(i=0;i<pno;i++)
    {
        for(j=0;j<bno;j++)
        {
            if(flag[j]==0&&bsize[j]>=psize[i])
            {
                flag[j]=1;
                allocation[j]=i;
                break;
            }
        }
    }
    printf("\nBlock no\tSize\t\tProcess no\tsize\n");
    for(i=0;i<bno;i++)
    {
        printf("%d\t\t%d",i+1,bsize[i]);
        if(flag[i]==1)
        {
            printf("\t\t%d\t\t%d\n",allocation[i]+1,psize[allocation[i]]);
        }
        else
        {
            printf("\t\tNot Allocated\n");
        }
    }

    getch();
    return 0;
}