# Creating the instance, you can change the number of points
m = RandomWalk(5000)
m.run_walk()

fig, ax = plt.subplots()

# Generating the plot
ax.scatter(m.x_values,m.y_values,c=m.y_values, cmap=plt.cm.magma, s=10)

# Titles and labels
ax.set_title("Random Walk", fontsize=20)
ax.set_xlabel("Values of X", fontsize=14)
ax.set_ylabel("Values of Y", fontsize=14)

ax.tick_params(labelsize=12)

ax.axis()

plt.style.use('dark_background')
plt.show()
