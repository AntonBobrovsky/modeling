#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#define COUNT_EVENTS 1000
#define EVENT0 0 /* A++*/
#define EVENT1 1 /* A--*/

int A = 0;

struct event {
    int type;
    float time;
    struct event *next;
    struct event *prev;
};

struct event *calendar;

struct event *pop()
{
	struct event *event = calendar;
	event->next->prev = NULL;
	calendar = event->next;
	return event;
}

void push(struct event *plan)
{
	struct event *event = calendar;
	if (NULL == calendar)
	{
		plan->next = NULL;
		plan->prev = NULL;
		calendar = plan;

		return;
	}
	while (NULL != event)
	{
		if (event->time > plan->time)
		{
			plan->next = event;
			plan->prev = event->prev;
			if (event->prev)
			{
				event->prev->next = plan;
			}
			else
			{
				calendar = plan;
			}
			event->prev = plan;
			return;
		}
		if (NULL == event->next) {
			plan->next = NULL;
			plan->prev = event;
			event->next = plan;

			return;
		}
		event = event->next;
	}
	return;
}

void schedule(int event, float curent_time)
{
	struct event *plan = malloc(sizeof(struct event));
	plan->time =  curent_time + (float)rand() / RAND_MAX;
	plan->type = event;
	push(plan);
}

void  run_implementation() {
    FILE *f;
    struct event *current_event;

    schedule(EVENT0, 0);
    schedule(EVENT1, 0);

    f = fopen("out", "w");
    for (int i = 0; i < COUNT_EVENTS; i++)
    {
        current_event = pop();
        if (current_event->type == EVENT0)
        {
            A++;
            schedule(EVENT0, current_event->time);
            fprintf(f, "%f\t%d\n", current_event->time, A );
        }
        else
        {
            A--;
            schedule(EVENT1, current_event->time);
            fprintf(f, "%f\t%d\n",  current_event->time, A);
        }
    }
    free(current_event);
}

int main(int argc, char const *argv[])
{
    srand(time(NULL));
    run_implementation();
	return 0;
}
