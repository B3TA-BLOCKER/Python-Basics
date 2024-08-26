# While Loops
# We can have the loop run indefinitely or (similar to an if statement) determine how many times the loop should run based on a condition.
i = 1
while i <= 10:
     print(i)
     i = i + 1




# For Loops
# A for loop is used to iterate over a sequence such as a list. Lists are used to store multiple items in a single variable, and are created using square brackets (see below).
websites = ["facebook.com", "google.com", "amazon.com"]
for site in websites:
     print(site)




#  Python code that will print the numbers from 0 to 4. In programming, 0 is often the starting number, so counting to 5 is 0 to 4 (but has 5 numbers: 0, 1, 2, 3, and 4)
for i in range(5):
     print(i)





# On the code editor, click back on the "script.py" tab and code a loop that outputs every number from 0 to 50.
for i in range(0,51):
  print(i)
# The flag is: THM{L00PS_WHILE_FOR}
