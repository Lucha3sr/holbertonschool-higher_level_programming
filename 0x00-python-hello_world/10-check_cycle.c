#include "lists.h"

/**
 * check_cycle - frees a listint_t list
 * @list: pointer to list
 * Return: void
 */
int check_cycle(listint_t *list)
{
	listint_t *p1 = list;
	listint_t *p2 = list;

	if (list == NULL)
	{
		return (0);
	}
	while (p1->next != NULL && p2->next != NULL)
	{
		p1 = p1->next;
		p2 = p2->next;
		if (p2->next == NULL)
		{
			return (0);
		}
		p2 = p2->next;
		if (p1 == p2)
		{
			return (1);
		}
	}
	return (0);
}
