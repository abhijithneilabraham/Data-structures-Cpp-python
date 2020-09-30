#include<iostream>

struct node
{
	int val;
	struct node *next;
};

struct node *temp, *front=NULL, *rear = NULL;

void insert(int data)
{
	temp = new struct node;
	temp->val = data;
	if(front==NULL && rear==NULL)
	{
		front=temp;
	}
	if(rear!=NULL)
	{	
		rear->next = temp;
	}
	rear=temp;
}

void del()
{
	temp = front;
	if(front!=NULL)
	{
		front = front->next;
		if(front==NULL)
			rear = NULL;
		std::cout<<temp->val<<"\n";
		delete temp;
	}
	else
		std::cout<<"\nStack Empty\n\n";
}

void display()
{
	temp = front;
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
	std::cout<<"commands: description\n";
	std::cout<<"insert <value> : inserts value into the queue\n";
	std::cout<<"delete : deletes from front of queue\n";
	std::cout<<"display : displays elements of the queue\n";
	std::cout<<"quit : quits program\n\n";
	do
	{
		std::cout<<"Enter command:  ";
		std::cin>>ch;
		if(ch.compare("insert")==0)
		{	
			std::cin>>a;
			insert(a);
		}
		else if(ch.compare("delete")==0)
			del();
		else if(ch.compare("display")==0)
			display();
		else if(ch.compare("quit")==0)
			break;
		else
			std::cout<<"\nInvalid command\n\n";
	}while(1);
}