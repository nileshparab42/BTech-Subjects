#include<stdio.h>
#include<conio.h>
#include<graphics.h>
float sm[3][3]={0},nm[3][10],om[3][10];
int i,j,v;
void main()
	{
	int gd= DETECT, gm;
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
	printf("\nEnter sx and sy\n");
	scanf("%f%f",&sm[0][0],&sm[1][1]);
	initgraph(&gd,&gm,"");
	for(i=0;i<v-1;i++)
		{
		line(om[0][i],om[1][i],om[0][i+1],om[1][i+1]);
		}
	line(om[0][v-1],om[1][v-1],om[0][0],om[1][0]);
	sm[2][2]=1;
	for(i=0;i<v;i++)
		{
		for(j=0;j<3;j++)
			{
			nm[j][i]= om[0][i]*sm[j][0] + om[1][i]*sm[j][1] + om[2][i]*sm[j][2] ;
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















