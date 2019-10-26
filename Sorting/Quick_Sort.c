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
 printf("Enter Elements One After Another :-\n\n");
 
 for(i=0;i<num;i++)
  scanf("%d",&arr[i]);

 printf("Elements In Unsorted Order :-\n\n");
 for(i=0;i<num;i++)
  printf("%d\n",arr[i]);

 QuickSort(arr,0,num);

 printf("Elements In Sorted Order :-\n\n");

 Print(arr,num);

 return 0;
}

void QuickSort(int arr[], int l, int r)           //arr[l...(r-1)]
{
 if((r-1) - l <=0)                           //Base Case : if there is only one element, then return
  return;

 int small=l+1,large;

 for(large=l+1;large<r;large++)
  {
   if(arr[large] <= arr[l])       //arr[l] is the pivot element
    {
     swap(&arr[large],&arr[small]);
     small++;
   }
  }
 swap(&arr[l],&arr[small-1]);

 QuickSort(arr,l,small-1);          //Recursive steps to sort left and right halves
 QuickSort(arr,small,r);
}

void swap(int *x, int *y)
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
 
