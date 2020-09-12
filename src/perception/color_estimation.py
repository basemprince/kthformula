from __future__ import print_function
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import numpy as np
import cv2
from collections import Counter
from skimage.color import rgb2lab, deltaE_cie76
import os
import webcolors

show_chart = False


def closest_colour(requested_colour):
    min_colours = {}
    for key, name in webcolors.css3_hex_to_names.items():
        if name in ['blue','yellow','black']:
            r_c, g_c, b_c = webcolors.hex_to_rgb(key)
            rd = (r_c - requested_colour[2]) ** 2
            gd = (g_c - requested_colour[1]) ** 2
            bd = (b_c - requested_colour[0]) ** 2
            min_colours[(rd + gd + bd)] = name
    return min_colours[min(min_colours.keys())]

def get_colour_name(requested_colour):
    try:
        closest_name = actual_name = webcolors.rgb_to_name(requested_colour)
    except ValueError:
        closest_name = closest_colour(requested_colour)
        actual_name = None
    return closest_name


def masking(image):
    imageHSV = cv2.cvtColor(image,cv2.COLOR_RGB2HSV)
    H = [0,179]
    S = [83,255]
    V = [0,255]
    lower_limit = np.array([H[0],S[0],V[0]])
    upper_limit = np.array([H[1],S[1],V[1]])
    mask = cv2.inRange(imageHSV, lower_limit, upper_limit)
    masked_image = cv2.bitwise_and(image,image,mask=mask)
    #cv2.imshow("masked",masked_image)
    #cv2.waitKey(0)
    return masked_image

def get_color(image,filename,number_of_colors):
    
    masked_image = masking(image)
    modified_image = cv2.resize(masked_image, (600, 400), interpolation = cv2.INTER_AREA)
    modified_image = modified_image.reshape(modified_image.shape[0]*modified_image.shape[1], 3)
    clf = KMeans(n_clusters = number_of_colors)
    labels = clf.fit_predict(modified_image)
    counts = Counter(labels)
    center_colors = clf.cluster_centers_
    # We get ordered colors by iterating through the keys
    ordered_colors = [center_colors[i] for i in counts.keys()]
    hex_colors = [RGB2HEX(ordered_colors[i]) for i in counts.keys()]
    rgb_colors = [ordered_colors[i] for i in counts.keys()]
    color_name = []
    for i in range (len(rgb_colors)):
        closest_name = get_colour_name(rgb_colors[i])
        color_name.append(closest_name)
        if(rgb_colors[i][0]>20 and rgb_colors[i][1]>20 and rgb_colors[i][2]>20):
            print (filename, " , closest cone colour is:", closest_name,sep= ' ')

    
    if (show_chart):
        plt.figure(figsize = (8, 6))
        plt.pie(counts.values(), labels = color_name, colors = hex_colors)
        plt.show()
    return rgb_colors

def RGB2HEX(color):
    return "#{:02x}{:02x}{:02x}".format(int(color[2]), int(color[1]), int(color[0]))


def pull_images(IMAGE_DIRECTORY):
    images = []
    filename = []
    for file in os.listdir(IMAGE_DIRECTORY):
        if file.endswith('.png'):
            image = cv2.imread(os.path.join(IMAGE_DIRECTORY, file))
            #image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            #cv2.imshow("image",image)
            #cv2.waitKey(0)
            images.append(image)
            filename.append(file)
    return images,filename

images = []
number_of_colors=2
images,filenames= pull_images('cone_images')
for i in range (len(images)):  
    rgb_color=get_color(images[i],filenames[i],number_of_colors)