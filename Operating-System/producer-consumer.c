#include<stdio.h>
#include<conio.h>
#include<stdlib.h>
void producer();
void consumer();
int mutex=1,isempty=10,isfull=0,x;
int main()
{
    int c,a=1;
    while(a=1){
    printf("1.Producer 2.Consumer 3.Exit\n");
    printf("Enter choice :\n");
    scanf("%d",&c);
    switch(c)
    {
        case 1:
        {
            if(mutex==1&&isempty!=0){
                producer();
            }
            break;
        }
        case 2:
        {
            if(mutex==1&&isfull!=0){
                consumer();
            }
            break;
        }
        case 3:
        {
            exit(0);
            a=0;
            break;
        }
    }}
    getch();
    return 0;
}
void producer()
{
    mutex--;
    isfull++;
    isempty--;
    x++;
    printf("Producer produces item %d\n",x);
    mutex++;
}
void consumer()
{
    mutex--;
    isempty++;
    isfull--;
    printf("Consumer consumes item %d\n\n",x);
    x--;
    mutex++;
}