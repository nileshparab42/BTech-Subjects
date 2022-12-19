//IMPLEMENT QUEUE ADT USING ARRAY
#include<stdio.h>
#include<conio.h>
void enqueue();
int dequeue();
void display();
int queue[100],front=-1,rare=-1,i,x=0,len;
void main()
	{
	int ch=1,ele;
	printf("Enter length of queue :");
	scanf("%d",&len);
	printf("----------MENU ----------");
	printf("\n1:enqueue\n2:dequeue\n3:Display\n0:Exit\n");
	printf("-------------------------\n");
	while(ch!=0){
			printf("choice->");
			scanf("%d",&ch);
			switch(ch)
				{
				case 1:
					{
					printf("enqueue->");
					scanf("%d",&ele);
					enqueue(ele);
					break;
					}
				case 2:
					{
					printf("Deleted element: %d\n",dequeue());
					break;
					}
				case 3:
					{
					display();
					break;
					}
				case 0:
					{
					break;
					}
				default :
					{
					printf("Enter valid choice !\n");
					}
				}
			}
	getch();
	clrscr();
	}
  //--------------------ENQUEUE FUNCTION---------------------------
	void enqueue(int a)
		{
		if(rare==len-1)
			{
			printf("Queue is full !");
			}
		else if(rare==-1)
			{
			front=0;
			rare=0;
			queue[rare]=a;
			}
		else
			{
			rare++;
			queue[rare]=a;
			}
		}
 //----------------------DEQUEUE FUNCTION---------------------------
	int dequeue()
		{
		if(front==-1)
			{
			printf("Queue is empty!");
			x=0;
			}
		else if(front==rare)
			{
			x=queue[front];
			front=-1;
			rare=-1;
			}
		else
			{
			x=queue[front];
			front++;
			}
		return x;
		}
 //----------------------DISPLAY FUNCTION-----------------------
	void display()
		{
		if(front==-1)
			{
			x=0;
			printf("Queue is empty!\n");
			}
		else
			{
			printf("Queue :\n");
			for(i=front;i<=rare;i++)
				{
				printf("%d\n",queue[i]);

				}
			}
		}
 //-----------------END OF THE PROGRAM--------------------------
