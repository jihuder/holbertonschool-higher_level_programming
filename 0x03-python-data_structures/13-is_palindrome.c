#include "list.h"
/**
 * is_palindrome - Check if the list is a palindrome
 * @head: Receive List
 * Return: returns 1 or 0 depending on whether there is a list
*/
int is_palindrome(listint_t **head)
{
	listint_t *previous = NULL, *next_¡ = NULL;
	unsigned int lenght = 0, place = 0, i = 0;

	next_¡ = *head;
	while (next_¡)
	{
		nex_¡ = next_¡->next;
		lenght++;
	}
	previous = *head;
	while (place != lenght / 2)
	{
		next_¡ = *head;
		if (place != 0)
			previous = previous->next;
		for (i = 0; i < lenght - (place + 1); i++)
			next_¡ = next_¡->next;
		if (next_¡->n != previous->n)
			return (0);
		place++;
	}
	return(1);
}
