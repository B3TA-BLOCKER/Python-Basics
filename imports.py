# In Python, we can import libraries, which are a collection of files that contain functions.
import datetime
current_time = datetime.datetime.now()
print(current_time)


# We import other libraries using the import keyword. Then in Python, we use that import's library name to reference its functions. 
# In the example above, we import datetime, then access the .now() method by calling library_name.method_name(). Copy and paste the example above into the code editor.

# Here are some popular libraries you may find useful in scripting as a pentester:

# Request - simple HTTP library.
# Scapy - send, sniff, dissect and forge network packets
# Pwntools - a CTF & exploit development library.
# Many of these libraries are already built into the programming language; however, 
# libraries written by other programmers not already installed in your machine can be installed using an application called pip, which is Python's package manager.
# Let's say you want to install the "scapy" library (which allows you to craft your own packets in code and send them to other machines); 
# you install it first by running the command pip install scapy, after which in your program you can now import the scapy library.
