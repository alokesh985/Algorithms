#include <stdio.h>

void swap(int*,int*);

int main()
{
 int num,i,j;
 printf("Enter Number Of Elements In Array : \n");
 scanf("%d",&num);
 int arr[num];
 printf("Enter Elements Of Array one after another : \n");
 for(i=0;i<num;i++)
  scanf("%d",&arr[i]);
 printf("Unsorted Array :- \n\n");
 for(i=0;i<num;i++)
  printf("%d\n",arr[i]);

 for(i=0;i<(num-1);i++)		//Bubble Sort Complexity O(n^2)
  for(j=0;j<(num-1-i);j++)
   {
    if(arr[j]>arr[j+1])
       swap(&arr[j+1],&arr[j]);
   }

 printf("Sorted Array :- \n\n");
 for(i=0;i<num;i++)
  printf("%d\n",arr[i]);

 return 0;
}

void swap(int *a, int*b)
{
 int temp=*a;
 *a=*b;
 *b=temp;
}
