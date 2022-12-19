#include<stdio.h>
#include<conio.h>
#include<graphics.h>
#include<math.h>
#include<dos.h>
void main()
	{
	float dx,dy,x,y,step,xinc,yinc,i;
	int x1,y1,x2,y2,gd=DETECT,gm;
	//----------------taking co-ordinates from user-------------------
	printf("Enter starting co-ordinates of line :");
	scanf("%d%d",&x1,&y1);
	printf("Enter endimg co-ordinates of line :");
	scanf("%d%d",&x2,&y2);
	//----------------Calculating length of line on x and y-----------
	dx=x2-x1;
	dy=y2-y1;
	//----------------------Calculating steps-------------------------
	if(abs(dx)>=abs(dy))
		{
		step=abs(dx);
		}
	else
		{
		step=abs(dy);
		}
	//----------------Calculating rate of change of x and y------------
	xinc=dx/step;
	yinc=dy/step;
	x=x1;
	y=y1;
	//-----------------------Ploting graph-----------------------------
	initgraph(&gd,&gm,"");
	putpixel(x,y,WHITE);
	for(i=1;i<step;i++)
		{
		x=x+xinc;
		y=y+yinc;
		x1=x+0.5;
		y1=y+0.5;
		putpixel(x1,y1,WHITE);
		}
	getch();
	closegraph();
	clrscr();
	}















