// Circular Queue Implementation

#include <stdio.h>
#include <stdlib.h>
#define MAX 4 // 4 elements in Queue

void enqueue(int[], int*, int*);
void dequeue(int[], int*, int*);
void print(int[], int*, int*);

int main()
{
    int queue[MAX];
    int choice;
    int front, rear;
    front = rear = -1;

    while(1)
    {
        printf("1. ENQUEUE\n2. DEQUEUE\n3. PRINT\n4. EXIT\n");
        scanf("%d", &choice);

        switch (choice)
        {
        case 1: enqueue(queue, &rear, &front);
            break;
        
        case 2: dequeue(queue, &rear, &front);
            break;

        case 3: print(queue, &rear, &front);
            break;

        case 4: printf("Exiting\n");
                exit(0);
            break;

        default: printf("INVALID OPTION ENTERED\n");
            break;
        }
    }
}

void enqueue(int queue[], int* rear, int* front)
{
    if(*rear == MAX - 1 && *front == 0)
    {
        printf("Queue Overflow\n");
    }

    else
    {
        printf("Enter Element to be enqueued: \n");
        int ip;
        scanf("%d", &ip);

        if(*rear == -1 && *front == -1)
        {
            queue[0] = ip;
            *rear += 1;
            *front += 1;
        }

        else
        {
            *rear = (*rear + 1) % MAX;
            queue[*rear] = ip;
        }
    }
}

void dequeue(int queue[], int* rear, int* front)
{
    if(*front == -1)
        printf("Queue Underflow\n");

    else
    {
        if(*front == *rear)
        {
            printf("Element Removed: %d\n", queue[*front]);
            *front = -1;
            *rear = -1;
        }
        
        else
        {
            printf("Element Dequeued: %d\n", queue[*front]);
            *front = (*front + 1) % MAX;
            
        }
        
    }
}

void print(int queue[], int* rear, int* front)
{
    if(*front == -1)
        printf("Queue Empty!\n");

    else
    {
    int i;
    for(i = *front; i != *rear; i = (i + 1) % MAX)
        printf("%d ", queue[i]);
    printf("%d ", queue[i]);

    printf("\n");
    }
}