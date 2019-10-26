#include <stdio.h>

int main()				//Complexity O(n)
{
 int num,i,search,flag=0;
 printf("Enter Number Of Elements In Array :\n");
 scanf("%d",&num);
 int arr[num];
 printf("Enter Elements One By One Followed : \n");
 for(i=0;i<num;i++)
  scanf("%d",&arr[i]);
 printf("Enter Number To Be Searched : \n");
 scanf("%d",&search);
 for(i=0;i<num;i++)
 {
  if(arr[i]==search)
   {
    flag=1;
    break;
   }
 }
 if(flag==1)
  printf("Element Found At Position %d\n",(i+1));
 else
  printf("Element Not Found in the List.\n");
 return 0;
}
 
   
