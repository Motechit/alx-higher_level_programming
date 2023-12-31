#include "lists.h"

/**
 * check_cycle - This fxn helps to check whether a linked list contains a cycle
 * @list: This is the linked list to be checked
 * Return: It returns 1 if the list has a cycle, 0 if otherwise
 */

int check_cycle(listint_t *list)
{
	listint_t *slow = list;
	listint_t *fast = list;

	if (!list)
		return (0);

	while (slow && fast && fast->next)
	{
		slow = slow->next;
		fast = fast->next->next;
		if (slow == fast)
			return (1);
	}

	return (0);
}
