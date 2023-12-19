import numpy as np

LEFT = 0
RIGHT = 1
END_NODE = "ZZZ"


if __name__ == "__main__":
    # Read puzzle input
    with open("./input.txt", "r") as file:
        lines = [line.strip() for line in file.readlines()]

    # Read directions
    directions = lines[0]
    directions = [LEFT if direction == "L" else RIGHT for direction in directions]

    # Construct adjacency dictionary
    nodes = lines[2:]
    adjacency_dict = {}
    for node in nodes:
        source_node = node[:3]
        dest_node_1, dest_node_2 = [
            dest_node.strip() for dest_node in node[7:-1].split(",")
        ]
        adjacency_dict[source_node] = (dest_node_1, dest_node_2)

    ## Part 1
    # Traverse network
    n_steps = 0
    current_node = "AAA"
    while current_node != END_NODE:
        direction = directions[n_steps % len(directions)]
        next_node = adjacency_dict[current_node][direction]
        current_node = next_node
        n_steps += 1

    print(f"The solution for part 1 is: {n_steps}")

    ## Part 2: find the lowest common multiple of all of the path lengths
    #          of each individual path
    starting_nodes = [node for node in adjacency_dict.keys() if node[-1] == "A"]

    n_steps = []
    for starting_node in starting_nodes:
        n_steps_i = 0
        current_node = starting_node
        # Traverse network
        while not current_node[-1] == "Z":
            direction = directions[n_steps_i % len(directions)]
            next_node = adjacency_dict[current_node][direction]
            current_node = next_node
            n_steps_i += 1
        n_steps.append(n_steps_i)
    lcm = np.lcm.reduce(n_steps)
    print(f"The solution for part 2 is: {lcm}")
