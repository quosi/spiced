import numpy as np
import math
from statistics import mean

# k-mean clustering

# tuple containing data set
data = ((2.6, 4.6, "blue"), (3.7, 4.8, "red"), (2.3 , 4.3, "red"), (6.1, 4.6, "blue"), (7.3, 2.1, "red"), (5.0, 5.3, "red"), (9.2, 4.7, "blue"), (7.0, 3.4, "blue"), (2.3, 5.8, "blue"), (6.2, 5.2, "red"), (1.5, 5.5, "red"), (3.4, 2.1, "red"), (0.4, 4.2, "blue"), (6.1, 7.8, "red"), (5.4, 6.2, "blue"), (5.3, 5.6, "blue"), (1.6, 2.9, "blue"), (4.0, 7.3, "red"), (7.1, 2.9, "red"), (8.2, 3.2, "blue"))

# split data set into lists with data from each column or colour
data_length = len(data)
data_x = []
data_y = []
data_c = []
data_points =[]
data_x_red = []
data_y_red = []
data_x_blue = []
data_y_blue = []

def data_split(data):
    for data_point in data:
        x, y, c = data_point
        data_x.append(x)
        data_y.append(y)
        data_points.append([x,y])
        data_c.append(c)
        if c == "red":
            data_x_red.append(x)
            data_y_red.append(y)
        else:
            data_x_blue.append(x)
            data_y_blue.append(y)

# call data split function
data_split(data)

#task1 - calculate mean of both x and y
mean_x = np.mean(data_x)
print("mean value for x: ")
print(mean_x)
mean_y = np.mean(data_y)
print("mean value for y: ")
print(mean_y)

#task2 - calculate mean of x/y for red and blue points separately
def task2 ():
    blue_center_x = np.mean(data_x_blue)
    blue_center_y = np.mean(data_y_blue)
    red_center_x = np.mean(data_x_red)
    red_center_y = np.mean(data_y_red)
    blue_center = [blue_center_x, blue_center_y]
    red_center = [red_center_x, red_center_y]
    print("mean value for blue (x,y): ")
    print(blue_center)
    print("mean value for red (x,y): ")
    print(red_center)
    return (blue_center, red_center)
# call task2 function
blue_center, red_center = task2()

#task3 - calculate euclidean distance to blue_center and red_center
def task3 (b_center, r_center):
    b_distance =[]
    r_distance =[]
    for xy in data_points:
        b_distance.append(math.sqrt(sum([(a - b) ** 2 for a, b in zip(xy, b_center)])))
        r_distance.append(math.sqrt(sum([(a - b) ** 2 for a, b in zip(xy, r_center)])))

    print("Euclidean distance from data points to blue center point: ", b_distance)
    print("Euclidean distance from data points to red center point: ", r_distance)
    return(b_distance, r_distance)
# call task3 function
blue_distance, red_distance = task3(blue_center, red_center)

#task4 - relable points; closer to blue center become blue poits, closer to red center become red points
def task4 (b_distance, r_distance):
    print(data_c)
    data_label = data_c
    for i in range(0, len(data_label)):
        if b_distance[i] > r_distance[i]:
            data_label[i] = "red"
        else:
            data_label[i] = "blue"
    return data_label
# call task4 function
data_label = task4(blue_distance, red_distance)
print(data_label)
print("finish first iteration")

#task5 - repeat step 2-4 three times

# call functions to repeat task2 - task4

blue_center_n, red_center_n = task2()
blue_distance_n, red_distance_n = task3(blue_center_n, red_center_n)
data_label_n = task4(blue_distance_n, red_distance_n)
