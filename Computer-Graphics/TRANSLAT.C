#include<stdio.h>
#include<conio.h>
#include<graphics.h>
void translation();
int tm[3][3]={0},i,j,nm[3][10],v,z=0;
void main()
	{
	int om[3][10],gd= DETECT, gm;
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
				scanf("%d",&om[j][i]);
				}
			}
		}
	printf("\nEnter tx and ty\n");
	scanf("%d%d",&tm[0][2],&tm[1][2]);
	initgraph(&gd,&gm,"");
	for(i=0;i<v-1;i++)
		{
		line(om[0][i],om[1][i],om[0][i+1],om[1][i+1]);
		}
	line(om[0][v-1],om[1][v-1],om[0][0],om[1][0]);
	tm[0][0]=1;
	tm[1][1]=1;
	tm[2][2]=1;
	for(i=0;i<v;i++)
		{
		for(j=0;j<3;j++)
			{
			nm[j][i]= om[0][i]*tm[j][0] + om[1][i]*tm[j][1] + om[2][i]*tm[j][2] ;
			z=0;
			}
		}
	getch();
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















