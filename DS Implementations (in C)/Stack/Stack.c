#include <stdio.h>
#define MAX 15
#include <stdlib.h>

int push(int[], int);
int pop(int[], int);
void print(int[], int);

int main()
{
    int choice, SP = -1; // SP is stack pointer
    int stack[MAX];

    while(1)
    {
        printf("1. PUSH\n2. POP\n3. PRINT\n4. EXIT\n");
        scanf("%d", &choice);

        switch (choice)
        {
        case 1: SP = push(stack, SP);
            break;
        
        case 2: SP = pop(stack, SP);
            break;

        case 3: print(stack, SP);
            break;

        case 4: printf("Exiting\n");
                exit(0);
        
        default: printf("Invalid Option Entered\n");
            break;
        }
    }

    return 0;

}

int push(int stack[], int SP)
{

    
    if(SP == MAX - 1)
    {
        printf("Stack Overflow\n");
        return SP;
    }

    int ip;
    printf("Enter Element to be pushed: \n");
    scanf("%d", &ip);

    SP += 1;
    stack[SP] = ip;

    return SP;
    
}

int pop(int stack[], int SP)
{

    if(SP == -1)
    {
        printf("Stack Underflow\n");
        return SP;
    }

    printf("Popped Element: %d\n", stack[SP]);
    SP -= 1;
    return SP;
}

void print(int stack[], int SP)
{
    if(SP == -1)
    {
        printf("Stack Empty");
    }
    else
    {
        for(int i = 0; i <= SP; i++)
        {
            printf("%d, ", stack[i]);
        }
        printf("\n");

    }

}