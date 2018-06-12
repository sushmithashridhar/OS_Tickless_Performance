import matplotlib.pyplot as plt
 
# line 1 points
x1 = [19.429771,38.872594,40.775367,48.383345,57.844440,62.876945]
y1 = [1,2,3,4,8,12]
x2 = [21.454703,42.115726,37.049644,48.900413,60.495253,70.888406]
y2 = [1,2,3,4,8,12]
# plotting the line 1 points 
#plt.plot(label = "Tickless Performance")
plt.plot(x1, y1, color='green', linestyle='dashed', linewidth = 1,
         marker='o', markerfacecolor='blue', markersize=8, label = "Tickless Performance")

plt.plot(x2, y2, color='green', linestyle='dashed', linewidth = 1,
         marker='o', markerfacecolor='red', markersize=8, label = "Ticked  Performance")

 
# line 2 points
# plotting the line 2 points 
#plt.plot(x2, y2, label = "Huey Performance")
 
# naming the x axis
plt.xlabel('Computation speed of the CPU [in terms of Giga IOPs]')
# naming the y axis
plt.ylabel('Number of threads')
# giving a title to my graph
plt.title('The example performs 100000000 IOPs using threads')
 
# show a legend on the plot
plt.legend()

image = "Performance Plot IOPS" 
plt.savefig(image)

# function to show the plot
plt.show()
