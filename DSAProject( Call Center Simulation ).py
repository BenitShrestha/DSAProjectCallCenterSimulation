import random # Importing Libraries
import simpy
import numpy as np 

# Initialize necessary parameters
No_of_Operator = 3
Average_Support_Time = 5
Customer_Interval = 2 
Sim_Time = 120 # Assume all time is in minutes
No_of_Customers_Handled = 0

env = simpy.Environment() # Generating simulation environment

class CallCenter:
    # Constructor to initialize call center parameters
    def __init__(self, env, no_of_operator, support_time):
        
        self.env = env
        self.no_of_operator = simpy.Resource(env, no_of_operator) # Limited no. of staff exist so it is a resource that can be used only when its available
        self.support_time = support_time
    
    
    # Support function that randomizes support time using random and numpy library
    def Support(self, customer_no):
        
        rand_time = max(1, np.random.normal(self.support_time, 5))
        yield self.env.timeout(rand_time)
        print(f"Support for customer {customer_no} was finished successfully at {self.env.now:.2f} mins from start of simulation.\n")


# Customer function defines customer behaviour in the simulation based on availability of operator and utilizes the Support function
def Customer(env, customer_no, call_center):
    
    global No_of_Customers_Handled
    print(f"Customer {customer_no} enters waiting queue at {env.now:.2f} mins from start of simulation.\n")
    
    with call_center.no_of_operator.request() as reqst: # Requests resource (an operator) from the class CallCenter
        yield reqst # Pauses execution of function (generator) until requested resource becomes available
        
        print(f'Customer {customer_no} has entered the call at {env.now:.2f} mins from start of simulation.\n')
        yield env.process(call_center.Support(customer_no)) # Runs Support function as a process in the simulation
        
        print(f'Customer {customer_no} has left the call at {env.now:.2f} mins from start of simulation.\n') 
        No_of_Customers_Handled += 1
        
        
def Setup(env, no_of_operator, support_time, customer_interval):
    
    call_centerobj = CallCenter(env, no_of_operator, support_time)
    
    for customer_no in range(1, 4): # Assumes that 3 customers are intially waiting for service
        env.process(Customer(env, customer_no, call_centerobj))
        
    while True: # Runs infintely until simulation is over (Simulation time is over)
        yield env.timeout(random.randint(customer_interval-1, customer_interval+1)) # Randomizes the customer interval by -1 or +1 in the simulation
        customer_no += 1
        
        env.process(Customer(env, customer_no, call_centerobj))


print('Initiating Call Center Simulation: \n')

env.process(Setup(env, No_of_Operator, Average_Support_Time, Customer_Interval)) # Calling Setup as a process in the simulation environment 
env.run(until=Sim_Time) # Run time of simulation provided
 
print(f'\nNumber of customer that were handled is {No_of_Customers_Handled}.')      