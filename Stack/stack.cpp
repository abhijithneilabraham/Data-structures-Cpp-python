#include<iostream>
#include<cstdio>

struct node
{
	int val;
	struct node *next;
};

struct node *temp, *top=NULL;

void push(int data)
{
	temp = new struct node;
	temp->val = data;
	if(top!=NULL)
		temp->next = top;
	top=temp;
}

void pop()
{
	temp = top;
	if(top!=NULL)
	{
		top = top->next;
		std::cout<<temp->val<<"\n";
		delete temp;
	}
	else
		std::cout<<"\nStack Empty\n";
}

void display()
{
	temp = top;
	while(temp!=NULL)
	{
		std::cout<<temp->val<<" ";
		temp = temp->next;
	}
	std::cout<<"\n";
}

int main()
{
	std::string ch;
	int a;
	std::cout<<"commands: \n";
	std::cout<<"push <value>\n";
	std::cout<<"pop \n";
	std::cout<<"display \n\n";
	std::cout<<"quit";
	do
	{
		std::cout<<"Enter command:  ";
		std::cin>>ch;
		if(ch.compare("push")==0)
		{	
			std::cin>>a;
			push(a);
		}
		else if(ch.compare("pop")==0)
			pop();
		else if(ch.compare("display")==0)
			display();
		else if(ch.compare("quit")==0)
			break;
		else
			std::cout<<"\nInvalid command\n";
	}while(1);
}