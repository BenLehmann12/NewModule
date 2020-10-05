'''
:param message: This is my Message
:param n: This is the number of times the message will be multiplied
:returns: Returns the String n times
'''

def multiply_string(message,n):
    multiply = message*n
    return multiply

if __name__ == "__main__":
    print(multiply_string("Ayah",3))