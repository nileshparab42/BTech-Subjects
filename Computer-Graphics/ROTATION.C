#include<stdio.h>
#include<conio.h>
#include<graphics.h>
#include<math.h>
float rm[3][3]={0},nm[3][10],om[3][10],t;
int i,j,v;
void main()
	{
	int gd= DETECT, gm;
	//----------------taking polygone from user-------------------
	printf("How many vertex polygone have :");
	scanf("%d",&v);
	for(i=0;i<v;i++)
		{
		printf("\nEnter X%d and Y%d\n",i+1,i+1);
		for(j=0;j<=2;j++)
			{
			if(j==2)
				{
				om[j][i]=1;
				}
			else
				{
				scanf("%f",&om[j][i]);
				}
			}
		}
	//----------------taking angle of rotation--------------------
	printf("\nEnter angle :\n");
	scanf("%f",&t);
	//---------------creating rotational matrix-------------------
	rm[0][0]=cos(t/180*3.14159);
	rm[0][1]=sin(t/180*3.14159);
	rm[1][0]=-sin(t/180*3.14159);
	rm[1][1]=cos(t/180*3.14159);
	rm[2][2]=1;

	initgraph(&gd,&gm,"");
	//--------------------Display old polygone--------------------
	for(i=0;i<v-1;i++)
		{
		line(om[0][i],om[1][i],om[0][i+1],om[1][i+1]);
		}
	line(om[0][v-1],om[1][v-1],om[0][0],om[1][0]);
	//--------------------generating new matrix-------------------
	for(i=0;i<v;i++)
		{
		for(j=0;j<3;j++)
			{
			nm[j][i]= om[0][i]*rm[j][0] + om[1][i]*rm[j][1] + om[2][i]*rm[j][2] ;
			}
		}
	getch();
	//-------------------Display new polygone---------------------
	setcolor(RED);
	for(i=0;i<v-1;i++)
		{
		line(nm[0][i],nm[1][i],nm[0][i+1],nm[1][i+1]);
		}
	line(nm[0][v-1],nm[1][v-1],nm[0][0],nm[1][0]);
	getch();
	closegraph();
	clrscr();
	}















