import matplotlib.pyplot as plt
from fontTools.merge import cmap

from random_walk import RandomWalk
while True:
    # Make a random walk.
    rw = RandomWalk(5000)
    rw.fill_walk()

    # Plot the points in the walk.
    plt.style.use('classic')
    fig, ax = plt.subplots(figsize=(15, 6), dpi=125)
    point_numbers = range(rw.num_points)
    # ax.scatter(rw.x_values, rw.y_values, s=1, c=point_numbers, cmap=plt.cm.Blues, edgecolor='none')
    ax.plot(rw.x_values, rw.y_values, linewidth=1, c='pink')

    # Emphasize the first and last points.
    ax.scatter(0, 0, c='green', edgecolor='none', s=100)
    ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolor='none', s=100)

    plt.show()

    keep_running = input("Make another walk? (y/n): ")
    if keep_running == 'n':
        break
