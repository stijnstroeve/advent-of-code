# Today's challenge:
# Finish the code because part 2 of this one look quite hard

def read_file(path):
    with open(path) as file:
        lines = file.readlines()
        file.close()

        return [line.strip() for line in lines]


orbit_map = read_file('map.txt')

def run():
    left = []
    right = []

    def get_individual_orbits(orbit_map):
        for orbit in orbit_map:
            split_orbit = str(orbit).split(')')

            left.append(split_orbit[0])
            right.append(split_orbit[1])

    def get_children(orbit):
        indices = [i for i, x in enumerate(left) if x == orbit]
        children = []

        for i in indices:
            children.append(right[i])

        return children

    def get_parents(orbit):
        indices = [i for i, x in enumerate(right) if x == orbit]
        parents = []

        for i in indices:
            parents.append(left[i])

        return parents

    def get_connected(orbit):
        return list(get_children(orbit) + get_parents(orbit))

    get_individual_orbits(orbit_map)

    explored = []
    robots = [('YOU', 0)]

    running = True

    while running:
        for i, robot in enumerate(robots):
            current_orbit, steps = robot
            connected = get_connected(current_orbit)
            if len(connected) > 0:
                del robots[i]

            for connection in connected:
                if connection not in explored:
                    total_steps = steps + 1
                    robots.append((connection, total_steps))
                    explored.append(connection)
                    if connection == 'SAN':
                        print(f'Santa is {total_steps} orbits away')
                        running = False
                        break

run()


# Had to redo almost the entire code, so not really quick
