import Task
import parse
import random

def random_generate_input_file(num_inputs):
    """
    Randomly generates an input file according to num_inputs
    """
    tasks = []
    for i in range(1, num_inputs + 1):
        deadline = random.randint(1, 1440)
        duration = random.randint(1, 60)
        perfect_benefit = round(random.random() * 100, 3)
        task = Task.Task(task_id=i, deadline=deadline, duration=duration, perfect_benefit=perfect_benefit)
        tasks.append(task)
    parse.write_input_file("randomized_input_example", tasks)

n = 100

random_generate_input_file(n)
