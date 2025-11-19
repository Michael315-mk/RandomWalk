# Creating the instance, you can change the number of points
m = RandomWalk(5000)
m.run_walk()

fig, ax = plt.subplots()

# List with the index numbers
list_index = range(m.total)

# Generating the plot
ax.scatter(m.x_values,m.y_values,c=list_index, cmap=plt.cm.magma, edgecolors='none', s=10)

# Titles and labels
ax.set_title("Random Walk", fontsize=20)
ax.set_xlabel("Values of X", fontsize=14)
ax.set_ylabel("Values of Y", fontsize=14)

ax.tick_params(labelsize=12)

ax.set_aspect('equal')
plt.style.use('dark_background')
plt.show()
