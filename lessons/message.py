"""Class to store a message (operator overload, union types, default parameters)"""

class Message: 

    to: str
    content: str
    important: bool

    def __init__(self, recipient: str, message_content: str, importance_flag: bool) -> None:
        """Constructing a message."""
        self.to = recipient 
        self.content = message_content
        self.important = importance_flag

# String method is going to help make our output more readable 
# As of now, when we print a function it says "The object is at "alphanumeric code"

    def __str__(self) -> str:
        output: str = f"Message to {self.to}:\n"
        output += f"Important? {self.important}\n"
        output += f'"{self.content}"'
        return output
    
    def __mul__(self, factor: int):
        """Multiplication operator overload."""
        copy_val: str = self.content
        for loop_number in range(1, factor):
            self.content += "" + copy_val
        

# If you want double quotes inside your strig then you must start your string with single quotes and then put double inside 

msg: Message = Message("Erin", "Great Job!", False)
msg * 7
msg_to_myself: Message = Message("me", "Do your homework!", True)
msg_to_myself * 12
print(msg_to_myself)
print(msg)