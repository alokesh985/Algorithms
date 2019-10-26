#include <stdio.h>

int Binary(int[],int,int,int);				//Complexity O(log(n))

int main()
{
 int num,search,i,result,start=0,end;
 printf("Enter Number Of Elements In Array : \n");
 scanf("%d",&num);
 int arr[num];
 printf("Enter Elements One By One In a sorted manner : \n");
 for(i=0;i<num;i++)
  scanf("%d",&arr[i]);
 
 printf("Enter Element to be searched :\n");
 scanf("%d",&search);
 end=num-1;
 
 result=Binary(arr,start,end,search);

 if(result==0)
  printf("Number Not Found!\n");
 else
  printf("Number Founds At Position %d\n",(result+1));

 return 0;
}


int Binary(int arr[],int start,int end, int search)
{
 int mid;
 if(start==end)
 { 
 if(arr[start]==search)
   return start;
  else
   return 0;
 }
 mid=(start+end)/2;
 if(arr[mid]==search)
  return mid;
 if(search<arr[mid])
  return (Binary(arr,start,mid-1,search));
 else
  return (Binary(arr,mid+1,end,search));
 }
