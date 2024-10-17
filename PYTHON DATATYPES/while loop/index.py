#syntax
"""
while condition:
    # code block to be executed
"""
# Example 1: Print numbers from 1 to 5
count = 1  # Step 1: Initialize count to 1

while count <= 5:  # Step 2: Start the while loop, the loop will run as long as count is <= 5
    print(count)  # Step 3: Print the current value of count
    count += 1  # Step 4: Increment count by 1

"""
line by line explanation
Explanation (Line by Line):
count = 1:
We initialize a variable count and assign it the value 1. This will serve as our loop control variable, which helps decide how long the loop runs.
while count <= 5::
The loop will keep running as long as the value of count is less than or equal to 5. This is the condition of the loop.
If count becomes greater than 5, the condition will evaluate to False, and the loop will stop.
print(count):
Inside the loop, this line will print the current value of count each time the loop executes.
count += 1:
This increments the value of count by 1 after each iteration. This ensures that eventually, count becomes greater than 5 and the loop stops.



"""