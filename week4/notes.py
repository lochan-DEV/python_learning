# day 1 of learning week 4 lecture 

# What is a library / module?
# A module is a file with pre-written code (functions)
# that you can import and use in your own code
# Instead of writing everything from scratch!
                 
#                   example:import random        # import whole module


""" Command-Line Arguments - Command-line arguments are inputs provided to a program 
                             when it is executed from the terminal. They allow users
 to pass data directly at runtime instead of entering it during execution."""



# day 2 of learning week 4 lecture

# IndexError -  happens when you try to access an index that doesn't exist.
# slicing - is a way to access a portion of a sequence (like a string, list, or tuple)


# day 3  
""" revised all previous lectures topics and solved week 4 problems """

"""sys.exit() - Lets you stop the program right there and then. You can pass a message too —
                 it prints it as an error message. Way cleaner than just crashing.

     if len(sys.argv) != 2:
        sys.exit("Usage: python greet.py name")"""

"""7. APIs and the requests Library
This is where it gets really cool. An API (Application Programming Interface) lets your Python program talk to the internet — grab live data from websites, weather services, etc.
-requests is a third-party library — need to pip install it first
-requests.get(url)  — sends a GET request to a URL and returns a response
-response.json()  — converts the response to a Python dictionary
-response.raise_for_status()  — throws an error if the request failed (e.g. 404)
    import requests
    response = requests.get("https://wttr.in/London?format=3")
    response.raise_for_status()
    print(response.text)   # London: ⛅ +15°C"""


