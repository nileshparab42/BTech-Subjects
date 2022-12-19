//IMPLEMENT STACK ADT USING ARRAY
#include<stdio.h>
#include<conio.h>
void push();
int pop();
void display();
int stack[100],top=-1,i,x=0,len;
void main()
	{
	int ch=1,ele;
	printf("Enter length of stack :");
	scanf("%d",&len);
	printf("----------MENU ----------");
	printf("\n1:Push\n2:Pop\n3:Display\n0:Exit\n");
	printf("-------------------------\n");
	while(ch!=0){
			printf("choice->");
			scanf("%d",&ch);
			switch(ch)
				{
				case 1:
					{
					printf("push->");
					scanf("%d",&ele);
					push(ele);
					break;
					}
				case 2:
					{
					printf("Deleted element: %d\n",pop());
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
  //--------------------PUSH FUNCTION---------------------------
	void push(int a)
		{
		if(top==len-1)
			{
			printf("Stack is full!\n");
			}
		else
			{
			top++;
			stack[top]=a;
			}
		}
 //----------------------POP FUNCTION---------------------------
	int pop()
		{
		if(top==-1)
			{
			x=0;
			printf("Stack is empty!\n");
			}
		else
			{
			x=stack[top];
			top--;
			}
		return x;
		}
 //----------------------DISPLAY FUNCTION-----------------------
	void display()
		{
		if(top==-1)
			{
			x=0;
			printf("Stack is empty!\n");
			}
		else
			{
			printf("Stack :\n");
			for(i=top;i>=0;i--)
				{
				printf("%d\n",stack[i]);
				}
			}
		}
 //-----------------END OF THE PROGRAM--------------------------