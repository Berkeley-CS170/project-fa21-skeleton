import numpy as np
import parse
import Task


def random_generate_input_file(num_inputs, fname):
    """
    Randomly generates an input file according to num_inputs and writes to a
    file with name fname
    """
    indices = np.arange(1, num_inputs + 1)
    deadlines = np.random.randint(1, 1440, size=num_inputs)
    durations = np.random.randint(1, 60, size=num_inputs)
    perfect_benefits = np.round(np.random.uniform(0, 100, size=num_inputs), 3)

    tasks = [
        Task.Task(
            task_id=i,
            deadline=deadline,
            duration=duration,
            perfect_benefit=perfect_benefit,
        )
        for i, deadline, duration, perfect_benefit in zip(
            indices, deadlines, durations, perfect_benefits
        )
    ]

    parse.write_input_file(fname, tasks)


if __name__ == "__main__":
    for input_size in (100, 150, 200):
        random_generate_input_file(input_size, f"{input_size}.in")
