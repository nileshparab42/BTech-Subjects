#include<stdio.h>
#include<conio.h>
int main()
{
    float M=60,Weight=0,n=5,profit=0;
    int i;
    float vi[10]={30,40,90,77,45};
    float wi[5]={5,10,25,22,15};
    for(i=0;i<n;i++)
    {
        printf("v[%d] = %f\t",i,vi[i]);
    }
    printf("\n");
    for(i=0;i<n;i++)
    {
        printf("w[%d] = %f\t",i,wi[i]);
    }
    printf("\n");
    for(i=0;i<n;i++)
        {
                if(Weight+wi[i]<=M)
                {
                    profit=profit+vi[i];
                    printf("%f\n",profit);
                    Weight=Weight+wi[i];
                }
                else 
                {
                    wi[i]=(M-Weight)/wi[i];
                    vi[i]=vi[i]*wi[i];
                    profit=profit+vi[i];
                    printf("m %f\n",profit);
                    Weight=M;
                    i=n;
                }           
        }

    printf("Total profit = %f",profit);
    getch();
    return 0;
}
