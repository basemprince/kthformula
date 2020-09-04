# KTH FORMULA EXERCISES

Exercise 1: Design, develop and debug a ROS network
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

Exercise 2: Programming a data visualisation tool
* Created an excutable Python file that uses matplotlib to visualize a function
* The function is h ( t ) = 3 * pi * exp(-lambda [ t ] ) where lambda ( t ) = 5 * sin ( 2 * pi * 1 * t )
* The graph has a 'real-time'/live updated data visualisation
