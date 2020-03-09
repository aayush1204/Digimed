#include<stdio.h>
#include<conio.h>
#include<stdlib.h>
struct Node{
	int data;
	struct Node* next;
}*top;

void push(int a)
{
	struct Node *temp,*newnode;
	newnode=(struct Node *)malloc(sizeof(struct Node));
	newnode->data=a;
	newnode->next=NULL;
	if(top == NULL)
		top=newnode;
	else
	{
		newnode->next=top;
		top=newnode;
			}		
	
}

void pop()
{
	int val;
	val=top->data;
	struct Node* temp;
	temp=top;
	top=top->next;
	free(temp);
	printf("%d",val);
	
}

int main()
{
	int n;
	printf("Enter the decimal Number \n");
	scanf("%d",&n);
	
	int b=n,c;
	
	while(b!=0)
	{
		c=b%2;
		b=b/2;
		push(c);
		
	}
	printf("Binary Number- \n");
	
	while(top!=NULL)
	{
		pop();
	}
}
