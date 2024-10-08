# Pet Health Tracker

## Introduction

The Pet Health Tracker program was initiated in order to provide effective, on demand management of crucial health information for pets in response to the growing need among pet owners for an accessible and efficient solution. Considering the challenges associated with pet healthcare, including organizing and evaluating different aspects, such as vaccinations, health records, veterinary appointments and many more, this particular program aims to provide a user-friendly platform that ensures comprehensive management. By offering a centralized hub for pet health data, the program itself tends to strengthen the overall well-being of pets and motivate an active approach to healthcare, simultaneously constructing a stronger bond between pet owners and their beloved companions.

The Pet Health Tracker focuses primarily on several objectives, such as registration and authentication of the user, which enables pet owners to create their own accounts, ensuring secure access to the application. Another objective would be the management of the pet information, which allows users to add, store and manage information about their pets, including many details that vary from the pet’s name to its vaccination status. Additionally, this application provides the ability to actively track a pet's health record, which helps pet owners to maintain a detailed health history, forming a connection between quality of veterinary care and informed decision-making. Moreover there is an option to access and schedule the next veterinary appointment and track information about it as well. Apart from the mentioned benefits, there is a possibility to load and save user data and to access pet information, preventing data loss.

Secondary objectives of the following platform would be error handling and feedback to users. For instance, the mentioned objective would level up the user experience and guide a user through potential issues and prevent difficulties. Scalability would be one of the interesting objectives, because the benefit of it is actually the main future goal of many programmers and developers and that is code improvement and enhancement. Furthermore, documentation, support and responsiveness would complete the entire code and its needed functionalities.

In conclusion, the Pet Health Tracker strives to provide a reliable companion for pet owners. Available opportunity to continually improve the platform and the code itself offers a delightful experience for both pets and their devoted caregivers.

## Program Functionalities

### User Registration: 
This functionality is essential for users and their ability to set up their accounts with a username and password of their choice, which helps in creating a personalized and secure experience within the application. In addition, this particular process is crucial for user individual needs and maintenance of the privacy and security of user data.

### User Login: 
With the capability of using a simple username and password, users are allowed to gain access to certain data of their pets. The functionality itself ensures ease of use and is truly important for providing users with an option to manage their pet’s health records with minimal effort.

### Load and Save Users: 
The system effortlessly loads user data from the ‘users.txt’ file during the application startup simultaneously providing continuous experience for users. The behind-the-scenes functionality is far more important for observing and managing user data between application sessions, enhancing the overall reliability of the application itself. Additionally, with high efficiency the system saves user data to the ‘users.txt’ file. Key of this functionality is to prevent data loss and securely store user’s data for future use.

### Add Pet: 
Using the least amount of time and effort users add details about their pets, including names, breeds, vaccination status, etc. Because of that, this functionality is vital for users to keep an individualized health history for each of their pets, enabling effective tracking and management of them.

### Display Pet Information: 
Presenting users a clear and detailed overview of their pet’s information improves transparency, flexibility and easy monitoring. This functionality is essential for keeping pet owners up to date about their pet’s healthcare journey.

### Add Health Record: 
Users record and store multiple health events for their pets, including a non-limited amount of important details such as dates and brief descriptions. The importance of this functionality is actually the need for maintaining an organized and detailed record of possible, yet specific health incidents and the need for understanding those difficulties in a better way possible.

### Add Vaccination: 
After answering a question about whether or not the pet is vaccinated, a defined method and function incorporated within the ‘Pet’ class enables users to record vaccination events and get further information about the following subject.

### Add Appointment: 
The primary objective of this functionality is to construct and define a new method and function which users experience in the input part of the entire code, where they can add an appointment and insert several details about it, after which a particular message will be displayed and the program will proceed with the calculation of the next possible appointment.

### Calculate Next Appointment: 
Shortly after entering details of the appointment, the named functionality will calculate the future time period when the next appointment should occur and it will ensure that the pet owner gets noted whether he/she should consider taking his/her pet to the veterinary clinic.

### Exit Application: 
Provides users with a simple exit option, which ensures a clean and user-friendly application experience. For the convenience of a user and the ability to exit the platform easily when needed to, this functionality is a key element for that.

## Flowcharts

The Pet Health Tracker platform integrates pet care management into user’s daily lives. Below are visual representations of key processes within the application.

### User Registration Process:
Purpose: This flowchart illustrates the process of registering a new user in the Pet Health Tracker application.
Sequence:
User enters a username and password.
The system checks if the entered username already exists.
If the username is unique, a new user object is created.
The user object is added to the list of users.
The updated user list is saved to the ‘users.txt.’ file.
Registration is successful.

### User Login Process:
Purpose: This flowchart illustrates the process of user login in the Pet Health Tracker application.
Sequence:
User enters a username and password.
The system searches for a matching user in the list.
If a match is found, the user is logged in, and the current user variable is updated.
If no match is found, the system indicates an invalid login attempt.

### Add Pet Process:
Purpose: This flowchart illustrates the process of adding a new pet to a user's profile in the Pet Health Tracker application.
Sequence:
User provides information about the pet (name, breed, age, weight, vaccination status).
A new pet object is created with the provided information.
The new pet is added to the user’s list of pets.

### Display Pet Information Process:
Purpose: This flowchart illustrates the process of displaying information about a user's pet/pets in the Pet Health Tracker application.
Sequence:
User selects the option to display pet information.
The system retrieves and displays details for each pet, including name, breed, age, weight, vaccinations, health records, and appointments.

### Add Health Record or Vaccination Process:
Purpose: This flowchart illustrates the process of adding a health record or vaccination to a user's pet in the Pet Health Tracker application.
Sequence:
User selects the option to add a health record or vaccination.
User provides information about the pet, date, description, and record type.
The system adds the new record to the corresponding list in the pet’s profile.

### Schedule Appointment Process:
Purpose: This flowchart illustrates the process of scheduling and managing appointments for a user's pet in the Pet Health Tracker application.
Sequence:
User selects the option to schedule an appointment.
User provides information about the pet and the last veterinarian visit date.
The system adds a new appointment for the last vet visit and calculates the next appointment date.
The system displays a message about the next appointment date.

These flowcharts provide a visual representation of the key processes in the Pet Health Tracker application, helping users and developers understand the system's functionality and logic.

Comments and explanations in code are like signs that guide developers and programmers through the logic and purpose of each part. In the provided code, comments present the roles of classes and functions, making it easier to understand and modify the code for possible future purposes. This promotes readability and collaboration among developers.

## Comments and Explanations:

### Class Definitions: 
The ‘User’, ‘Pet’, ‘Record’, ‘Appointment’ classes represent the main entities in the overall system, containing user information, pet details, appointment details and health records.

### Loading and Saving Users: 
‘load_users()’ and ‘save_users()’ do certain tasks, where the first one reads user information from a particular file, and the second one writes that information to that file.

### User Registration and Login: 
‘register()’ firstly checks whether the username already exists, and if that is not the case, it registers a new user to the system. ‘login()’ logs in the already existing registered user and it checks whether the user credentials are valid or not.

### Adding Pet and Health Record: 
‘add_pet()’ and ‘add_record()’ functions allow users to add an unlimited amount of new pets and their health records.

### Adding Vaccinations and Appointments: 
‘add_vaccination’ and ‘add_appointment’ functions allow users to add a non-limited amount of detailed information about past or present vaccinations and appointments. 

### Calculating The Next Appointment: 
‘calculate_next_appointment’ function fulfills the code with the ability of calculating the date of the future veterinary appointment. 

### Displaying Pet Information: 
A detailed display of a user's pet and its important information is provided by the function ‘display_pet_info()’.

### Main Menu Loop: 
Several available options are displayed by the ‘main_menu()’ function which handles user input and executes actions based on the selected option.
