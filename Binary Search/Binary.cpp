#include<iostream>
using namespace std;
bool Binary(int data[],int target,int low,int high)
{
  int mid;
  mid=(low+high)/2;

if(low>high){
  return false;
}
else{
  if(target==data[mid]){
    return true; }
    else if(target<data[mid]){
      return Binary(data,target,low,mid-1);    }
      else{
        return Binary(data,target,mid+1,high);
      }

  }
}
int main()
{
int dat[]={1,8,4,5,3,2,4};
bool b;
b=Binary(dat,7,0,6);
cout<<b;
return 0;
}
