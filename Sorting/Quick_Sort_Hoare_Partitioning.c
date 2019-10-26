#include <stdio.h>

void QuickSort(int[],int,int);
void swap(int*,int*);
void Print(int[],int);

int main()
{
 int num;
 printf("Enter Number Of Elements In Array :\n");
 scanf("%d",&num);
 int arr[num],i;
 printf("Enter Elements Of Array one after another :-\n");
 for(i=0;i<num;i++)
  scanf("%d",&arr[i]);

 QuickSort(arr,0,num);

 printf("Sorted Array :-\n\n");
 Print(arr,num);

 return 0;
}

void QuickSort(int arr[],int l,int r)
{
 if((r-1)-l <= 0)
  return;

 int left,right;
 left=l+1,right=r-1;;
 int pivot=l;
 
 while(right>=left)
 {
  while(arr[left]<arr[pivot] && right>=left)
    left++;
  while(arr[right]>arr[pivot] && right >= left)
    right--;
  if(arr[left] > arr[right] && right >= left)
  {
   swap(&arr[left],&arr[right]);
   left++;
   right--;
  }
  
 }

 swap(&arr[right],&arr[pivot]);

 QuickSort(arr,l,right);
 QuickSort(arr,left,r);
}

void swap(int *x,int *y)
{
 int temp=*x;
 *x=*y;
 *y=temp;
}

void Print(int arr[],int num)
{
 for(int i=0;i<num;i++)
  printf("%d\n",arr[i]);
}
