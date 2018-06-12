import matplotlib.pyplot as plt
 
# line 1 points
x1 = [21.639649,43.253968,41.566944,50.116562,65.664800,65.117115]
y1 = [1,2,3,4,8,12]
x2 = [19.217000,37.761845,35.335348,46.239355,56.982030,66.148881]
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
plt.xlabel('GFLOPs')
# naming the y axis
plt.ylabel('Number of threads')
# giving a title to my graph
plt.title('The example performs 100000000 FLOPs using threads')
 
# show a legend on the plot
plt.legend()

image = "Performance Plot" 
plt.savefig(image)

# function to show the plot
plt.show()
