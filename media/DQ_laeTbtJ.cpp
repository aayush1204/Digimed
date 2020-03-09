#include<stdio.h>
#include<conio.h>
#include<stdlib.h>
int front=-1,rear=-1;
int q[5];

void enquerear()
{
	
	
	if(front==rear+1)
	{
		printf("queue full");
	}
	else
	{
		int val;
	printf("enter data to be added \n");
	scanf("%d",&val);
	if(rear==-1)
	{
		rear=0;
		front=0;
		q[rear]=val;
	}
	else{
		rear=(rear+1)%5;
		q[rear]=val;
	    }
	}
	
}

void enquefront()
{   //happens anticlockwise

	if(front==rear+1)
	{
		printf("queue full");
	}
	
	else
	{
	int val;
	printf("enter data to be added \n");
	scanf("%d",&val);
	if(front==-1)
	{
		rear=0;
		front=0;
		q[front]=val;
	}
	
	else{
		front=(front-1 + 5)%5;
		q[front]=val;
    	}
	}
	
	
}
void deletefront()
{
	int x;
	x=q[front];
	if(front==rear)
	{
		front=-1;
		rear=-1;
	}
	else
		front=(front+1)%5;
}

void deleterear()
{
	int x;
	x=q[rear];
	if(front==rear)
	{
		front=-1;
		rear=-1;
	}
	else
		rear=(rear-1+5)%5;
}

void display()
{
	int i=front;
	if(front==-1)
	{
		printf("Empty queue");
	}
	else
	{	printf("DQ- ");
		while(i!=rear)
		{
			printf("%d ,",q[i]);
			i=(i+1)%5;
		}
		printf("%d \n",q[i]); //important line
	}
	
}

int main()
{
	enquerear();
	enquerear();
	enquefront();
	enquefront();
	display();
//	deleterear();
//	display();
//	deletefront();
//	display();
	enquefront();
	enquerear();
	display();
	
}
