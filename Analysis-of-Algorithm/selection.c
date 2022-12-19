#include<stdio.h>
#include<conio.h>
int main()
{
    int i,j,temp,n,a[10],swap=0,min_pos;
    float wswap,pswap;
    printf("Insert array size :\n");
    scanf("%d",&n);
    printf("Insert elements :\n");
    for(i=0;i<n;i++)
    {
        scanf("\n%d",&a[i]);
    }
    for(i=0;i<n-1;i++)
    {
        min_pos=i;
        for(j=i+1;j<n;j++)
        {
            if(a[j]<a[min_pos])
            {
                min_pos=j;
            }
        }
        if(a[min_pos]!=a[i])
        {
            swap=swap+1;
            temp=a[i];
            a[i]=a[min_pos];
            a[min_pos]=temp;
        }
    }
    printf("\nAfter Sorting :");
    for(i=0;i<n;i++)
    {
        printf("\n%d",a[i]);
    }
    wswap=n-1;
    pswap=(swap/wswap)*100;
    printf("\n\n--------Analysis of algorithm :--------");
    printf("\nTotal swap : %d",swap);
    printf("\nPercentage of swap : %f percent",pswap);
    if(pswap<33)
    {
        printf("\nBest Case");
    }
    else if(pswap>33 && pswap<66)
    {
        printf("\nAverage Case");
    }
    else
    {
        printf("\nWorst case");
    }

    getch();
    return 0;
}