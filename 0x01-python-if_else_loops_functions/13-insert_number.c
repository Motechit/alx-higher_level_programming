#include "lists.h"

/**
 * insert_node - This fxn inserts a num into a sorted singly-linked list
 * @head: This is s ptr to the head of the linked list
 * @number: This is the num to be inserted
 * Return: It returns NULL if fxn fails, a ptr to the new node if otherwise
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *node = *head, *new;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = number;

	if (node == NULL || node->n >= number)
	{
		new->next = node;
		*head = new;
		return (new);
	}

	while (node && node->next && node->next->n < number)
		node = node->next;

	new->next = node->next;
	node->next = new;

	return (new);
}
