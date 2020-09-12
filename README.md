# KTH FORMULA EXERCISES

<b><u>Exercise 1:</u> Design, develop and debug a ROS network</b>
 
* Created a topic named after my surname "Shaker"
* Created a publisher "Talker", that sends a message:
  * the message type is UInt16
  * the starting number is random between 1 and 2^16
  * the message increases by n = 4
  * the message keeps increasing untill it reaches limit of UInt16 and resets to a random number
* Created a subscriber "Listener", that does the following:
  * receives the UInt16 message published to the "Shaker" topic
  * The message is then divided by 0.15 and then published to a new topic named "Result"
* Created plots for the "Shaker" and "Result" topics using PlotJuggler

<b>Exercise 2: Programming a data visualisation tool</b>
 
* Created an excutable Python file that uses matplotlib to visualize a function
* The function is h ( t ) = 3 * pi * exp(-lambda [ t ] ) where lambda ( t ) = 5 * sin ( 2 * pi * 1 * t )
* The graph has a 'real-time'/live updated data visualisation

# KTH FORMULA PERCEPTION TASKS
<b>Exercise 1: Colour estimation of cones</b>
 
* Created an excutable Python file that uses OpenCV and sklearn to look for specific colors (yellow/blue)
* The cone is already assumed extracted

<b>Exercise 2: Real-time cone detection on videos</b>

* The task is to put bounding boxes around cones on the video and indicate their color
* Tried the following (unsuccessful):
 * TensorFlow Object Detection API using this tutorial: https://www.youtube.com/watch?v=COlbP62-B-U
 * Train for custom object (with supplied pictures of cones) using the API w/ a pre-trained model
 * Hand labled the images using "labelImg.py" to produce XML files and split them into train and test samples
 * Generate a tf Record for the samples
 * Set-up a configuration file and train the actual model
 * Export the graph result and bring in that frozen enfrence graph and use to classify on the videos
