#include<stdio.h>
void swap(int *x1, int *x2){

int temp= *x1;
  *x1 = *x2;
  *x2 = temp;
}
void bubblesort(int arr[],int n){
  int i,j;
  bool swapped;
  for(i=0;i<n-1;i++)
  {
    swapped=false;
    for(j=i+1;j<=n;j++)
    {
      if(arr[j]>arr[j+1])
      {
        swap(&arr[j],&arr[j+1]);
        swapped=true;
      }
    }
      if(swapped==false){
        break;
      }
}
}
  int main()
  {
    int ar[]={1,3,2,4,5};
  int  num=5;
    bubblesort(ar, num);
    printf("Sorted array: \n");
    for(int i=0;i<num;i++)
    {
      printf("%d",ar[i]);

    }
    return 0;
  }
