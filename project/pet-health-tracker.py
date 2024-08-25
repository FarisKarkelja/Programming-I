'''
Project Subject: Pet Health Tracker

Build an application that allows pet  
owners to record and track their pet's
health records, vaccinations, and
appointments with veterinarians.
'''

# Define a class for users
class User:
    def __init__(self, username, password):
        self.username = username  # Each user has a username
        self.password = password  # Each user has a password
        self.pets = []  # Each user has a pet or a list of pets, which starts with an empty list

# Define a class for health records
class Record:
    def __init__(self, date, description):
        self.date = date  # Each health record has a date
        self.description = description  # Each health record has a description

# Define a class for appointments
class Appointment:
    def __init__(self, date, description):
        self.date = date  # Each appointment has a date
        self.description = description  # Each appointment has a description

# Define a class for pets
class Pet:
    def __init__(self, name, breed="Unknown", age=None, weight=None,
                 health_records=None, vaccinations=None, appointments=None):
        self.name = name  # Each pet has a name
        self.breed = breed  # Each pet has a breed. Default value of that breed is set to "Unknown" if not provided
        self.age = age  # Each pet has an age. Default value of that age is set to "Unknown" if not provided
        self.weight = weight  # Each pet has weight. Default value of that weight is set to "Unknown" if not provided

        # Each pet has a list of health records. If no records are provided, this starts as an empty list
        if health_records:
            self.health_records = health_records
        else:
            self.health_records = []

        # Each pet has a list of vaccinations. If no vaccinations are provided, this starts as an empty list
        if vaccinations:
            self.vaccinations = vaccinations
        else:
            self.vaccinations = []

        # Each pet has a list of appointments. If no appointments are provided, this starts as an empty list
        if appointments:
            self.appointments = appointments
        else:
            self.appointments = []

    # Define a function to add vaccination to a pet
    def add_vaccination(self, date, description):
        new_vaccination = Record(date, description)  # Create a new Record object
        self.vaccinations.append(new_vaccination)  # Add the new vaccination to the pet's list of vaccinations

    # Define a function to add an appointment to a pet
    def add_appointment(self, date, description):
        new_appointment = Appointment(date, description)  # Create a new Appointment object
        self.appointments.append(new_appointment)  # Add the new appointment to the pet's list of appointments

    # Define a function to calculate the next appointment date for a pet
    def calculate_next_appointment(self):
        if self.appointments: # Check if the pet has any previous appointments
            last_appointment = self.appointments[-1] # Get the date of the last appointment
            last_date = last_appointment.date

            # Extract components of the last appointment date
            date_components = last_date.split('-')
            year = int(date_components[0])
            month = int(date_components[1])
            day = int(date_components[2])

            next_month = month + 1 # Calculate the month of the next appointment

            if next_month > 12: # Handle the case where the next month goes beyond December
                next_month = 1 # Reset to January
                year += 1 # Edit the year for the next appointment

            next_appointment_date = f"{year:04d}-{next_month:02d}-{day:02d}" # Formulate the next appointment date in YYYY-MM-DD format

            return next_appointment_date
        else:
            return None  # If the pet has no previous appointments, return None

# Create an empty list to store all users
users = []

# Define a function to load users from a particular file
def load_users():
    try:
        with open('users.txt', 'r') as f:
            for line in f:
                username, password = line.strip().split(',')
                users.append(User(username, password))  # Create a User object for each line of the file where users are stored
    except FileNotFoundError:
        print("No users found.")  # If the file does not exist, the output will be an error message

# Define a function to save users in a particular file
def save_users():
    with open('users.txt', 'w') as f:
        for user in users:
            f.write(f"{user.username},{user.password}\n")  # Write each user's username and password to the file

# Define a function to register a new user
def register(username, password):
    for user in users:
        if user.username == username:
            return "Username already exists."  # If the username already exists, return a message
    new_user = User(username, password)  # Create a new User object
    users.append(new_user)  # Add the new user to the list of users
    save_users()  # Save the updated list of users to the file
    return "Registration successful."  # Return a success message

# Define a function to log in a user
def login(username, password):
    for user in users:
        if user.username == username and user.password == password:
            return user  # If the username and password match a user in the list, return the User object
    return None  # If the username and password do not match a user in the list, return None

# Define a function to add a pet to a user
def add_pet(user):
    pet_name = input("Enter the name of your pet: ")
    pet_breed = input("Enter the breed of your pet: ")
    pet_age = input("Enter the age of your pet: ")
    pet_weight = input("Enter the weight of your pet: ")
    pet_vaccination = input("Is your pet vaccinated? (yes/no): ").lower()

    if pet_vaccination == 'no':
        print("It is recommended to vaccinate your pet. Consult your veterinarian for more information.")

    new_pet = Pet(pet_name, pet_breed, pet_age, pet_weight, [], [], [])  # Create a new Pet object
    user.pets.append(new_pet)  # Add the new pet to the user's list of pets

# Define a function to add a health record to a pet
def add_record(pet, date, description):
    new_record = Record(date, description)  # Create a new Record object
    pet.health_records.append(new_record)  # Add the new record to the pet's list of health records

# Define a function to schedule and manage appointments
def schedule_appointment(user):
    pet_name = input("Enter the name of your pet: ")
    last_vet_visit = input("Enter the last date your pet visited the veterinarian (YYYY-MM-DD): ")

    for pet in user.pets: # Search for the pet in the user's list of pets
        if pet.name == pet_name:
            pet.add_appointment(last_vet_visit, "Last Vet Visit") # Add a new appointment for the last vet visit

            next_appointment_date = pet.calculate_next_appointment() # Calculate the next appointment date
            if next_appointment_date:
                print(f"Don't forget to visit the vet often. Your next appointment for {pet_name} should be scheduled for {next_appointment_date}") # Display a message about the next appointment date
            else:
                print(f"Appointment for {pet_name} has been scheduled, but there is an issue calculating the next appointment date.")

            break #Exit the loop
    else:
        print(f"No pet found with the name {pet_name}.")

# Define a function to display information about a user's pet/pets
def display_pet_info(user):
    for pet in user.pets:
        print(f"Pet Name: {pet.name}")
        print(f"Breed: {pet.breed}")
        print(f"Age: {pet.age}")
        print(f"Weight: {pet.weight}")

        # Display vaccination status
        if not pet.vaccinations:
            print("Vaccinated: Not Vaccinated")
        else:
            print(f"Vaccinated: {', '.join([f'{record.date}: {record.description}' for record in pet.vaccinations])}")

        print("Health Records:")
        for record in pet.health_records:
            print(f"Date: {record.date}, Description: {record.description}")

        print("Appointments:")
        for appointment in pet.appointments:
            print(f"Date: {appointment.date}, Description: {appointment.description}")

        print()  # Print an empty line between pets

# Define a function to display the main menu
def main_menu():
    print("=====================================")
    print("🐾 PET HEALTH TRACKER APPLICATION 🐾")
    print("=====================================")
    print("Please select an option from the menu:")
    print("1. Register")
    print("2. Login")
    print("3. Add Pet")
    print("4. Display Pet Info")
    print("5. Add Health Record or Vaccination")
    print("6. Schedule Appointment")
    print("7. Exit")

# Load the users from the file
load_users()

# Initialize a variable to keep track of the current user
current_user = None

# Start the main menu loop
while True:
    main_menu()  # Display the main menu
    option = input("Enter your option: ")  # Ask the user to select an option
    if option == '1':
        username = input("Enter a username: ")
        password = input("Enter a password: ")
        print(register(username, password))  # Register a new user
    elif option == '2':
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        current_user = login(username, password)  # Log in a user
        if current_user is None:
            print("Invalid username or password.")
        else:
            print(f"Welcome back, {username}!")
    elif option == '3':
        if current_user:
            add_pet(current_user)
        else:
            print("You need to login first.")
    elif option == '4':
        if current_user:  # If a user is logged in
            display_pet_info(current_user)  # Call the display_pet_info function to display the current user's pet info
        else:
            print("You need to login first.")
    elif option == '5':
        if current_user:
            pet_name = input("Enter the name of your pet: ")
            date = input("Enter the date of the record (YYYY-MM-DD): ")
            description = input("Enter a description of the record: ")
            record_type = input("Is this a health record or a vaccination? (health/vaccination): ")
            for pet in current_user.pets:  # For each pet in the current user's list of pets
                if pet.name == pet_name:  # If the pet's name matches the name provided by the user
                    if record_type.lower() == 'health':
                        add_record(pet, date, description)  # Call the add_record function to add a record for the pet
                        print(f"Health record for {pet_name} has been added.")
                    elif record_type.lower() == 'vaccination':
                        pet.add_vaccination(date, description)
                        print(f"Vaccination record for {pet_name} has been added.")
                    else:
                        print("Invalid record type. Please enter 'health' or 'vaccination'.")
                    break
            else:
                print(f"No pet found with the name {pet_name}.")  # If no pet with the provided name is found
        else:
            print("You need to login first.")  # If no user is logged in, print the following message
    elif option == '6':
        if current_user:
            schedule_appointment(current_user)
        else:
            print("You need to login first.")
    elif option == '7':
        print("Thank you for using the Pet Health Tracker. Goodbye!")
        break
    else:
        print("Invalid option. Please try again.")  # Print an error message