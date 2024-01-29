#include <stdio.h>
#include <sys/types.h>
#include <unistd.h>
#include <stdlib.h>
#include <sys/wait.h>

int infinite_while(void);
/**
 * main - function make zombie processe.
 *
 * Return: alway 0.
 */
int main(void)
{
	pid_t xxo;
	char kane = 0;

	while (kane < 5)
	{
		xxo = fork();
		if (xxo > 0)
		{
			printf("Zombie process created, PID: %d\n", xxo);
			sleep(1);
			kane++;
		}
		else
			exit(0);
	}

	infinite_while();

	return (EXIT_SUCCESS);
}
/**
 * infinite_while -  A function that runs an infinite loop with a 1-second delay.
 *
 * Return: Always 0.
 */
int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}
