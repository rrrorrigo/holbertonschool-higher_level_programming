#include "lists.h"
/**
 * is_palindrome - function that check if a linked list is palindrome
 * @head: double pointer to the linked list
 * Return: 1 if it is palindrome, 0 if isn't
 */
int is_palindrome(listint_t **head)
{
	listint_t *aux = *head;
	size_t size = 0, buffer[2024], i = 0;

	if (!(*head) || !(*head)->next)
		return (1);
	while (aux)
	{
		buffer[size] = aux->n;
		aux = aux->next;
		size++;
	}
	while (size >= i)
	{
		if (buffer[size - 1] != buffer[i])
			return (0);
		size--;
		i++;
	}
	return (1);
}
