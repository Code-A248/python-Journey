print("My Name is Code-A , What is your name ?")

Name = input("Enter your name : ")

print(f"Hello {Name} , Welcome to the world of Python Programming !")

Choices = input("Do you want to continue ? (Yes/No) : ")

message = "Thank you for your response !" if Choices.lower(
) == "no" else "Great ! Let's continue our journey in Python Programming !"

print(message)
