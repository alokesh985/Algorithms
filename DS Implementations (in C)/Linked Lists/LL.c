#include <stdio.h>
#include <stdlib.h>
struct node
{
    int data;
    struct node* next;
};

void print_LL(struct node*);

int main()
{
    struct node* head, *ptr, * save;
    head = NULL;

    int input;
    char choice = 'Y';

    while(choice == 'Y' || choice == 'y')
    {
        printf("Enter Element Number: \n");
        scanf("%d", &input);

        ptr = (struct node*)malloc(sizeof(struct node));
        ptr -> data = input;

        if(head == NULL)
        {
            head = ptr;
            save = ptr;
        }
        else
        {
            save -> next = ptr;
            save = ptr;
        }

        printf("Would You Like to add another element?\n");
        scanf(" %c", &choice);
    }

    print_LL(head);

    return 0;
}

void print_LL(struct node* head)
{
    struct node* ptr = head;

    while(ptr != NULL)
    {
        printf("%d --> ", ptr->data);
        ptr = ptr->next;
    }
}