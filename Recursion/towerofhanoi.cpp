#include<iostream>
using namespace std;
void towers(int,char,char,char);
int main()
{
  int num;
  cout<<"\nEnter the number of disks:";
  cin>>num;
  cout<<"\nThe sequences involved in moving from A to B:";
  towers(num,'A','B','C');
  return 0;
}
void towers(int num,char a,char b, char c){
  if(num==1)
  {
    cout<<"\nMove disk one from peg"<<a<<"to"<<c;
    return;
  }
  towers(num-1,a,b,c);
  cout<<"\n Move disk "<<num<<"from"<<a<<"to"<<c;
  towers(num-1,b,c,a);
}
