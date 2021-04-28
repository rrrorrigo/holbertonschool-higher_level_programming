#include "lists.h"
/**
 * insert_node -  inserts a number into a sorted singly linked list.
 * @head: struct of linked list
 * @number: integer to insert into linked list
 * Return: the address of the new node, or NULL if it failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *nodeToInsert;

	nodeToInsert = malloc(sizeof(listint_t));
	nodeToInsert->n = number;
	nodeToInsert->next = NULL;

	if (!(*head) || (*head)->n >= number)
	{
		nodeToInsert->next = *(head);
		return ((*head) = nodeToInsert);
	}

	while (*head)
	{
		if (!(*head)->next || (*head)->next->n > number)
		{
			nodeToInsert->next = (*head)->next;
			(*head)->next = nodeToInsert;
			return (nodeToInsert);
		}
		head = &(*head)->next;
	}
	return (NULL);
}
