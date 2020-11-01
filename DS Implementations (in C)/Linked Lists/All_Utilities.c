#include <stdio.h>
#include <stdlib.h>

struct node
{
    int data;
    struct node* next;
};

void print_LL(struct node*);
void AddEnd(struct node*, int);
struct node* DeleteFront(struct node*);
struct node* DeleteEnd(struct node*);
struct node* Reverse(struct node*);

void AddBefore(struct node*, int, int);

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

    // printf("Enter Element to add to end of the LL: \n");
    // int in_end;
    // scanf("%d", &in_end);
   
    // head = DeleteFront(head);
    /*AddEnd(head, in_end);*/

    // head = DeleteEnd(head);

    // printf("Enter Node to enter before: \n");
    // int node_before, ip;
    // scanf("%d", &node_before);
    // printf("Enter New Node: ");
    // scanf("%d", &ip);
    // AddBefore(head, node_before, ip);

    head = Reverse(head);

    print_LL(head);

    return 0;
}

struct node* Reverse(struct node* head)
{
    struct node* current = head, *previous = NULL, *next_node = NULL; /* Using 3 pointers */

    while(current != NULL)
    {
        next_node = current -> next;
        current -> next = previous;
        previous = current;
        current = next_node;
    }

    head = previous;
    return(head);
}

void AddBefore(struct node* head, int node_before, int ip)
{
    struct node* ptr = head;

    while(ptr -> next -> data != node_before)
    {
        ptr = ptr -> next;
    }

    struct node* new_node = (struct node*)malloc(sizeof(struct node));

    new_node -> data = ip;

    new_node -> next = ptr -> next;
    ptr -> next = new_node;
}

struct node* DeleteEnd(struct node* head)
{
    struct node* ptr = head;

    while(ptr -> next -> next != NULL)
    {
        ptr = ptr -> next;
    }
    
    struct node* to_delete = ptr -> next;
    ptr -> next = NULL;

    free(to_delete);
    to_delete = NULL;

    return head;

}

struct node* DeleteFront(struct node* head)
{
    struct node* ptr = head;
    head = head->next;
    free(ptr);
    ptr = NULL;

    return(head);
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