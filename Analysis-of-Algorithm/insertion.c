#include<stdio.h>
#include<conio.h>
int main()
{
    int i,j,temp,n,a[10],swap=0;
    float wswap,pswap;
    printf("Insert array size :\n");
    scanf("%d",&n);
    printf("Insert elements :\n");
    for(i=0;i<n;i++)
    {
        scanf("\n%d",&a[i]);
    }
    for(j=1;j<n;j++)
    {
        temp=a[j];
        i=j-1;
        while(i>=0 && temp<a[i])
        {
            a[i+1]=a[i];
            swap++;
            i--;
        }
        a[i+1]=temp;
    }
    printf("\nAfter Sorting :");
    for(i=0;i<n;i++)
    {
        printf("\n%d",a[i]);
    }
    wswap=(n*(n-1))/2;
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