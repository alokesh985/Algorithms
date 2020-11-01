#include <stdio.h>

void SelectionSort(int[], int);
void swap(int*,int*);

int main()
{
    printf("Enter Number of elements in array: \n");
    int n;
    scanf("%d", &n);

    int arr[n];

    for(int i = 0; i < n; i++)
    {
        printf("Enter element %d: \n", (i + 1));
        scanf("%d", &arr[i]);
    }

    SelectionSort(arr, n);

    printf("Sorted Array: \n");

    for(int i = 0; i < n; i++)
    {
        printf("%d\n", arr[i]);
        
    }

    return 0;
}

void SelectionSort(int arr[], int n)
{
    for(int i = 0; i < (n - 1); i++)
    {
        int min = i;

        for(int j = i + 1; j < n; j++)
        {
            if(arr[j] < arr[min])
                min = j;
        }
    swap(&arr[min], &arr[i]);
    }
}

void swap(int *x, int* y)
{
    int temp = *x;
    *x = *y;
    *y = temp;
}