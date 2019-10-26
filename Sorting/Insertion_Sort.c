#include <stdio.h>

void InsertionSort(int[],int);
void swap(int*,int*);

int main()
{
 int num;
 printf("Enter Number Of Elements In Array : \n");
 scanf("%d",&num);
 int arr[num],i;
 printf("Enter Elements Of Array one after another :-\n");
 for(i=0;i<num;i++)
  scanf("%d",&arr[i]);
 
 printf("Elements Of Unsorted Array :-\n\n");
 for(i=0;i<num;i++)
  printf("%d\n",arr[i]);

 InsertionSort(arr,num);

 printf("Elements Of Sorted Array :-\n\n");
 for(i=0;i<num;i++)
  printf("%d\n",arr[i]);

 return 0;
}

void InsertionSort(int arr[],int num)		//Complexity O(n^2)
{
 int pos,nextpos;
 for(pos=1;pos<num;pos++)
  {
   nextpos=pos;
   while(nextpos > 0 && (arr[nextpos]<arr[nextpos-1]))
    {
     swap(&arr[nextpos],&arr[nextpos-1]);
     nextpos-=1;
    }
  }
}

void swap(int *x, int *y)
{
 int temp=*x;
 *x=*y;
 *y=temp;
}
