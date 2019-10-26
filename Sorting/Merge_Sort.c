#include <stdio.h>

void Merge(int[],int,int,int);
void MergeSort(int[],int,int);
void Print(int[],int);

int main()
{

 int num;
 printf("Enter Number Of Elements In Array :\n");
 scanf("%d",&num);
 int arr[num],i;
 printf("Enter Elements Of Array One After Another :\n");
 
for(i=0;i<num;i++)
  scanf("%d",&arr[i]);

 int org_arr[num];
 for(i=0;i<num;i++)
  org_arr[i]=arr[i];               //Storing Original Array in org_array

 printf("Unsorted Array :-\n\n");  //Printing Unsorted Array
 for(i=0;i<num;i++)
  printf("%d\n",org_arr[i]);
  printf("\n");
                  

 MergeSort(arr,0,num-1);          //(num-1) because array indexing goes from 0 to (n-1)
 
 Print(arr,num);

 return 0;
}

void MergeSort(int arr[],int left, int right)
{
 if(left<right)                                   //(left < right) ensures that array has >1 elements                                               
 {
  int mid=(left+right)/2;
  
  MergeSort(arr,left,mid);                       //Recursive calls to reapeatedly divide the array
  MergeSort(arr,mid+1,right);
  Merge(arr,left,mid,right);                          
 }                            
}

void Merge(int arr[],int left, int mid, int right)
{

 int temp[right+1];                                //temp is a temporary array to sort the values
 int i=left,j=mid+1,k=left;
 
 while(i<=mid && j<=right)                         //(i<=mid) and (j<=right) ensures that both subarrays are not empty.
 {

  if(arr[i] < arr[j])
   temp[k++]=arr[i++];
  
  else
   temp[k++]=arr[j++];
 }
 while(i<=mid)                                 //This line puts the remaining elements of 1st subarray to the temporary array.
  temp[k++]=arr[i++];

 while(j<=right)
  temp[k++]=arr[j++];

 for(i=left;i<=right;i++)                     //Copying the temporary array to the required array.
  arr[i]=temp[i];
}


void Print(int arr[], int num)
{
 for(int i=0;i<num;i++)
  printf("%d\n",arr[i]);
}  
