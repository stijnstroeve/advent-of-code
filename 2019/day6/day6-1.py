import time

def read_file(path):
    with open(path) as file:
        lines = file.readlines()
        file.close()

        return [line.strip() for line in lines]

orbit_map = read_file('map.txt')

l1 = []
l2 = []

def get_individual_orbits(orbit_map):
    global l1, l2
    orbits = []
    for orbit in orbit_map:
        split_orbit = str(orbit).split(')')
        orbits.append(split_orbit[0])
        orbits.append(split_orbit[1])

        l1.append(split_orbit[0])
        l2.append(split_orbit[1])
    return set(list(orbits))

def figure_out_path(orbit):
    global l1, l2
    steps = 0
    current_orbit = orbit
    while current_orbit != 'COM':
        index = l2.index(current_orbit)
        companion = l1[index]
        current_orbit = companion
        steps += 1

    return steps

now = time.time()

individual = get_individual_orbits(orbit_map)
total_steps = 0
for orbit in individual:
    total_steps += figure_out_path(orbit)

print(f'Total steps: {total_steps}, time: {(time.time() - now)}')
