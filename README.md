This is a Call Center Simulation Project done using Python's Simpy library in conjuction with Random and Numpy libraries.
The project is based on the general operation of an actual call center i.e 1. Customer waits in queue to enter call, 2. Enters the call, 3. Gets support and it finishes in some time, 4. Customer leaves the call.
These 4 criteria need to be fulfilled for a customer to be considered handled by the Call Center
Simulation. Additionally, in the source code (.py file), the working of certain code segments/functions as well as other required form of documentation is present in form of comments. Likewise, with the use of Pyscript, the main code file (.py) was linked to a HTML file. This was done to observe the output of the .py file on a webpage by the use of a live server (search and download Live Server extension in VS Code or other IDE, then run the HTML file using it). 
About Call Center Simulation modifiable variables:
1. No. of operators - Total no. of staff that can attend to 1 customer at a time
2. Average Support time - Mean time for support provided to a customer by operator
3. Interval of customer arrival - Time interval in which customer arrives in the simulation for waiting in the queue
4. Simulation time - Total time for the simulation to run
All times are in minutes, example: simulation time of 60 means it runs for 60 minutes or 1 hr (not actual minutes but program based time computed by Simpy)
