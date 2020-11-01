#include <stdio.h>
#include <stdlib.h>
struct node
{
    int data;
    struct node* next;
};

void print_LL(struct node*);
void AddEnd(struct node*, int);

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

    printf("Enter Element to add to end of the LL: \n");
    int in_end;
    scanf("%d", &in_end);
   
    AddEnd(head, in_end);

    print_LL(head);

    return 0;
}

void AddEnd(struct node* head, int ip)
{
    struct node* new_node = (struct node*)malloc(sizeof(struct node));

    new_node -> data = ip;

    struct node* ptr = head;

    while(ptr -> next != NULL)
    {
        ptr = ptr->next;
    }

    ptr -> next = new_node;
}

void print_LL(struct node* head)
{
    struct node* ptr = head;

    while(ptr -> next != NULL)
    {
        printf("%d --> ", ptr->data);
        ptr = ptr->next;
    }
    printf("%d", ptr->data);
    printf("\n");
}