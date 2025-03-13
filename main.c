#include <unistd.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

struct PeopleList{
	int age;
	char *name;
	struct PeopleList *next;
};

struct PeopleList *createNode(int age, const char *name)
{
	struct PeopleList *newNode = malloc(sizeof(struct PeopleList));
	newNode = malloc(sizeof(struct PeopleList));
	if (!newNode)
		return (0);
	newNode->age = age;
	newNode->name = strdup(name);
	newNode->next = NULL;

	return newNode;

}

void printList(struct PeopleList *head)
{
	struct PeopleList *current = head;
	while (current != NULL)
	{
		printf("nom : %s, Age :%d \n", current->name, current->age);
		current = current->next;
	}

}

void pushFront(struct PeopleList **head, int age, const char *name)
{
	struct PeopleList *newNode = createNode(age, name);
	newNode->next = *head;
	*head = newNode;
}

int main(void)
{
	struct PeopleList *mylist = NULL;

	pushFront(&mylist ,25, "Toto");
	pushFront(&mylist ,18, "Tata");

	printList(mylist);
}
