#include <stdio.h>

void Insertion_Sort(int[],int);
void swap(int*,int*);

int main()
{
 int num;
 printf("Enter Number Of Elements In Array : \n");
 scanf("%d",&num);
 int arr[num],i;
 printf("Enter Elements Of Array one by one :-\n");
 for(i=0;i<num;i++)
  scanf("%d",&arr[i]);
 
 printf("Unsorted Array :-\n\n");
 for(i=0;i<num;i++)
  printf("%d\n",arr[i]);

 Insertion_Sort(arr,num);

 printf("Sorted Array :-\n\n");
 for(i=0;i<num;i++)
  printf("%d\n",arr[i]);

 return 0;
}

void Insertion_Sort(int arr[],int num)
{
 int min,start,i;
 for(start=0;start<(num-1);start++)
  {
   min=start;
   for(i=min+1;i<num;i++)
     if(arr[i]<arr[min])
       min=i;

  swap(&arr[start],&arr[min]);
 }
}
 
void swap(int *x,int *y)
{
 int temp=*x;
 *x=*y;
 *y=temp;
}
