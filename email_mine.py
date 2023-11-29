### --- OOP Email Simulator --- ###

# --- Email Class --- #
# Create the class, constructor and methods to create a new Email object.
class Email():
    # Declare the class variable, with default value, for emails. 
    has_been_read = False
     # Initialise the instance variables for emails.
    def __init__(self, email_address, subject_line, email_content):
        self.email_address = email_address
        self.subject_line = subject_line
        self.email_content = email_content
    # Create the method to change 'has_been_read' emails from False to True.
    def mark_as_read(self):
        self.has_been_read = True
    # create method to display email in a user friendly format for me
    def __str__(self):
        return f"From: {self.email_address}\nSubject: {self.subject_line}\nContent: {self.email_content}\nRead: {self.has_been_read}"
# --- Lists --- #
# Initialise an empty list to store the email objects.
class Inbox:
    def __init__(self):
        self.email_list = []
# --- Functions --- #
# Build out the required functions for your program.
    def populate_inbox(self):
       
       self.email_list.append(Email("1@example.com", "Welcome to HyperionDev!", "This is email 1 content.")) 
       self.email_list.append(Email("2@example.com", "Great work on Bootcamp!", "This is email 2 content.")) 
       self.email_list.append(Email("3@example.com", "Your excellent marks!", "This is email 3 content."))
      
       
    # Create 3 sample emails and add it to the Inbox list. 

    def list_emails(self):
    # Create a function which prints the email’s subject_line, along with a corresponding number.
        for i, email in enumerate(self.email_list):
            print (f"{i} {email.subject_line}")
        
    # Create a function which displays a selected email. 
    # Once displayed, call the class method to set its 'has_been_read' variable to True.
    def read_email(self, index):
        if 0 <= index < len(self.email_list):
            email = self.email_list[index]
            if not email.has_been_read:
                email.mark_as_read()
                print(email)

# --- Email Program --- #

# Call the function to populate the Inbox for further use in your program.
inbox = Inbox()
inbox.populate_inbox()

# List the emails in the inbox
print("List of emails in the inbox:")
inbox.list_emails()

# Fill in the logic for the various menu operations.
menu = True

while True:
    inbox.list_emails
    user_choice = int(input('''\nWould you like to:
    1. Read an email
    2. View unread emails
    3. Quit application

    Enter selection: '''))
       
    if user_choice == 1:
        # add logic here to read an email
        index_to_read = int(input("Enter the index of the email you want to read: "))
        inbox.read_email(index_to_read)

        
    elif user_choice == 2:
        # add logic here to view unread emails
        for i, email in enumerate(inbox.email_list):
            if not email.has_been_read:
                print(f"{i} {email.subject_line}")
            
    elif user_choice == 3:
        # add logic here to quit application
        print("Goodbye!")
        break

    else:
        print("Oops - incorrect input.")

