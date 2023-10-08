import random 
#add comments throughout!



flightsDataFileName = 'allFlights.txt'
flight_details_dictionary = {}
totalRowsInPlane = 5
totalColumnsInPlane = 4


#WRITING A FILE FUNCTION
def writeToFile():

    with open(flightsDataFileName, 'w') as file:
        file.write(str(flight_details_dictionary))


#READING A FILE FUNCTION
def readFromFile(file):

    with open(file, 'r') as file:
        stringDataInFile = file.read()
        global flight_details_dictionary   # declare flight_details_dictionary to be a global
        if stringDataInFile == "":
            flight_details_dictionary = {}

        else:
            flight_details_dictionary = eval(stringDataInFile)  # this sets the global value of flight_details_dictionary
           




#Random quotes that appear when user gets logged in
quotes = [
        "'FLYING ALLOWS YOU TO SEE THE WORLD FROM A DIFFERENT PERSPECTIVE.'",
        "'JETTING OFF TO NEW DESTINATIONS, ONE FLIGHT AT A TIME.'",
        "'AIRPLANES ARE TIME MACHINES THAT TAKE YOU TO DISTANT PLACES.'",
        "'THE THRILL OF TAKEOFF, THE BEAUTY OF BEING ABOVE THE CLOUDS.'",
        "'IN THE SKY, THERE ARE NO BORDERS, ONLY ENDLESS HORIZONS.'"
]


    

#DYNAMIC SEATING LAYOUT
def seating_layout():


  columnsDictionary = {"A": 0, "B": 1, "C": 2, "D": 3}

  seatingLayout = []

  for i in range(totalRowsInPlane):
      row = []
      for j in range(totalColumnsInPlane):
        row.append("O")
      seatingLayout.append(row)

  return seatingLayout



#WORKING WITH ADMIN FUNCTIONS

def AddFlight():


    print("\nTo add a flight into our database, you need to enter the subsequent details.")
    print()
    airlines = str(input("Enter airlines name: "))

    if airlines in flight_details_dictionary:
        print("\nThis airline has been already added in the system! ")

    else:
        flight_number = str(input("Enter flight number: "))
        layout = seating_layout()
        departure_city = str(input("Enter departure city: "))
        arrival_city = str(input("Enter arrival city: "))
        aircraft = str(input("Enter aircraft: "))
        departure_time = str(input("Enter departure time: "))
        arrival_time = str(input("Enter arrival time: "))
        flight_duration = str(input("Enter the flight duration: "))

        newFlight = {
            "Flight Number" : flight_number,
            "Seating Layout" : layout,
            "Departure City" : departure_city,
            "Arrival City" : arrival_city,
            "Aircraft" : aircraft,
            "Departure Time" : departure_time,
            "Arrival Time" : arrival_time,
            "Flight Duration" : flight_duration,
            "Seating Layout" : layout

        }

        
        flight_details_dictionary[airlines] = newFlight
        
        writeToFile()

        print()
        print("Dear admin, your flight has been entered into the system!")



def modifyFlightDetails(admin_input):
    
        
    while True:    
        
        print("\nModify the flight details you want, admin.")
        print("\n1. Flight Number;")
        print("\n2. Departure City;")
        print("\n3. Arrival City;")
        print("\n4. Aircraft;")
        print("\n5. Departure Time;")
        print("\n6. Arrival Time;")

        selectedOption = str(input("\nEnter the relevant number you want to modify, admin. "))

        modifiedFlightDict = flight_details_dictionary[admin_input]

        if selectedOption == "1":
            newFlightNumber = input("Enter the new Flight Number: ")
            modifiedFlightDict["Flight Number"] = newFlightNumber
            flight_details_dictionary[admin_input] = modifiedFlightDict
            break


        elif selectedOption == "2":
            newDepartureCity = input("Enter the new Departure City: ")
            modifiedFlightDict["Departure City"] = newDepartureCity
            flight_details_dictionary[admin_input] = modifiedFlightDict
            break

        elif selectedOption == "3":
            newArrivalCity = input("Enter the new Arrival City: ")
            modifiedFlightDict["Arrival City"] = newArrivalCity
            flight_details_dictionary[admin_input] = modifiedFlightDict
            break

        elif selectedOption == "4":
            newAircraft = input("Enter the new Aircraft Name: ")
            modifiedFlightDict["Aircraft"] = newAircraft
            flight_details_dictionary[admin_input] = modifiedFlightDict
            break


        elif selectedOption == "5":
            newDepartureTime = input("Enter the new Departure Time: ")
            modifiedFlightDict["Departure Time"] = newDepartureTime
            flight_details_dictionary[admin_input] = modifiedFlightDict
            break

        elif selectedOption == "6":
            newArrivalTime = input("Enter the new Arrival Time: ")
            modifiedFlightDict["Arrival Time"] = newArrivalTime
            flight_details_dictionary[admin_input] = modifiedFlightDict
            break

        else:
            print("\nInvalid option, please select a valid option.")



    writeToFile()
    print("\nDear admin, your modification has been successfully updated!")



def showSystemFlightsForModification():


    #the admin will be able to modify the flight details here, except the seating layout

    if len(flight_details_dictionary) == 0:
        print("\nThere is no pre-existing flight in the system.")

    else:
        
        print("\nWhich flight do you want to modify?")
        print()
        
        
        for flight in flight_details_dictionary:
            print(flight)
            print()

        while True: 

            admin_input = input("\nEnter the flight name: ")

            if admin_input in flight_details_dictionary:
                modifyFlightDetails(admin_input)
                break

            else:
                print("\nInvalid entry, please enter the correct spellings for the modification.") #check


def removeFlight(admin_input):


    del flight_details_dictionary[admin_input]

    writeToFile()

    print("\nYour stated flight has been removed from the system.")



def showSystemFlightsForRemoval():


    if len(flight_details_dictionary) == 0:
        print("\nThere is no pre-existing flight in the system.")

    else:
        print("\nWhich flight do you want to delete?")
        print()

        for flight in flight_details_dictionary:
            print(flight)
            print()

        while True: 

            admin_input = input("\nEnter the flight name: ")

            if admin_input in flight_details_dictionary:
                removeFlight(admin_input)
                break

            else:
                print("\nInvalid entry, please enter the correct spellings in order to remove the flight.")



#ADMIN INTERFACE WHEN ADMIN GETS LOGGED IN

def admin_interface(admin_name):

    while True:
   
        print("\nWELCOME", admin_name + "!")
        print()
        selectedOption = str(input('''\nSelect any one of the options below: 
\n1. ADD AN AIRLINE FLIGHT;
2. MODIFY AN AIRLINE FLIGHT;
3. REMOVE AN AIRLINE FLIGHT.
4. LOG OUT TO MAIN MENU.                                   
'''))
        
        

        if selectedOption == "1":
            AddFlight() 
           
        
        elif selectedOption == "2":
            showSystemFlightsForModification()
            

        elif selectedOption == "3":
            showSystemFlightsForRemoval()


        elif selectedOption == "4":
            break
            

        else:
            print("Invalid entry, please select only one of the three options!")



#WORKING WITH USER FUNCTIONS

def bookingTicket():

    # user to be shown options which flights are available

    if len(flight_details_dictionary) == 0:
        print("\nThere is no pre-existing flight in the system.")

    else:

        print("\nDear user, please select an airline booking from the available flights.")
        print()
        for flight in flight_details_dictionary:
            print(flight)
            print()


        while True: 

            user_input = str(input("\nEnter your selected flight option: "))
            
            if user_input not in flight_details_dictionary:
                print("\nInvalid entry for the flight, please enter the correct spellings.")

            else:
                print("\nDear user, view the seating layout for the flight.")
                print()

                selectedFlightDictionary = flight_details_dictionary[user_input]

                selectedFlight2DLayout = selectedFlightDictionary["Seating Layout"]

                print("        A B C D")
                for row in range(len(selectedFlight2DLayout)):
                    print("Row", row + 1, ":",  end = " ")
                    for column in selectedFlight2DLayout[row]:
                        print(column, end=" ")
                    print()

                break



        userInputName = str(input("\nPlease enter your name: "))

        while True:
            userRow = int(input("\nEnter your preferred row number: "))
            userColumn = str(input("Enter your preferred seat letter(A, B, C or D): "))  

            columnsDictionary = {"A": 0, "B": 1, "C": 2, "D": 3}

            if userRow < 0 or userRow > 6:
                print("\nInvalid entry, please enter a valid row.")



            elif userColumn == "A" or userColumn == "B" or userColumn == "C" or userColumn == "D":

                if selectedFlight2DLayout[userRow - 1][columnsDictionary[userColumn]] == "X":
                    print("\nThis seat has already been booked, please try again. Thank you!")
                

                else:
                    selectedFlight2DLayout[userRow -1][columnsDictionary[userColumn]] = "X"

                    selectedFlightDictionary["Seating Layout"] = selectedFlight2DLayout

                    flight_details_dictionary[user_input] = selectedFlightDictionary

                    writeToFile()

                    print("\nAn airline flight of " + user_input + " has been booked by the name " + userInputName + " with row number " + str(userRow) + " and seat " + userColumn + ".")

                    break 
                

            else:
                print("\nInvalid entry, please enter a valid column.")
                    


def cancellingBooking():


    if len(flight_details_dictionary) == 0:
        print("\nThere is no pre-existing flight in the system.")

    else:
    
        print("\nDear user, please select an airline booking from the available flights that you want to cancel.")
        print()
        for flight in flight_details_dictionary:
            print(flight)
            print()

        while True: 

            user_input = str(input("\nEnter your selected flight option: "))
            
            if user_input not in flight_details_dictionary:
                print("\nInvalid entry for the flight, please enter the correct spellings.")

                

            else:

                selectedFlightDictionary = flight_details_dictionary[user_input]

                selectedFlight2DLayout = selectedFlightDictionary["Seating Layout"]

                break


        while True:

            userRow = int(input("\nEnter your booked row number: "))
            userColumn = str(input("Enter your booked seat letter(A, B, C or D): "))  

            columnsDictionary = {"A": 0, "B": 1, "C": 2, "D": 3}

            if userRow < 0 or userRow > 6:
                print("\nInvalid entry, please enter a valid row.")


            elif userColumn == "A" or userColumn == "B" or userColumn == "C" or userColumn == "D":

                if selectedFlight2DLayout[userRow - 1][columnsDictionary[userColumn]] == "X":

                    selectedFlight2DLayout[userRow - 1][columnsDictionary[userColumn]] = "O"

                    selectedFlightDictionary["Seating Layout"] = selectedFlight2DLayout

                    flight_details_dictionary[user_input] = selectedFlightDictionary

                    writeToFile()

                    print("\nThe booked flight has been cancelled.")

                    break

                else:
                    print("\nThe given seat is already vacant.")

                    break

            else:
                print("\nInvalid entry, please enter a valid column.")

  



def allFlightsAvailable():


    if len(flight_details_dictionary) == 0:
        print("\nThere is no pre-existing flight in the system.")

    else:

        print("\nDear user, these are the existing available flights in the system.")
        print()

        for flight, details in flight_details_dictionary.items():
            print(f"\nFlight: {flight}\n")
            for key, value in details.items():
                if key == "Seating Layout":
                    continue
                print(f"{key}: {value}")



#USER INTERFACE WHEN USER GETS LOGGED IN

def user_interface(user_name):

    while True:
   
        print("\nWELCOME", user_name + "!")
        print()
        print("Quote of the day: ", random.choice(quotes))
        selectedOption = str(input("\nWe hope you are having a great day, select any one of the options below:\n\n1. BOOK AN AIRLINE TICKET;\n2. CANCEL AN AIRLINE BOOKING;\n3. VIEW ALL AIRLINE FLIGHT DETAILS;\n4. LOG OUT TO MAIN MENU. "))
        

        if selectedOption == "1":
            bookingTicket() 
            

        elif selectedOption == "2":
            cancellingBooking()
             

        elif selectedOption == "3":
            allFlightsAvailable()


        elif selectedOption == "4":
            break
             

        else:
            print("Invalid entry, please select only one of the three options!")




#Dealing with user (option 1)
def user_login():

    while True:

        existing_user_logins = {
                        "mateenrehman" : "qwerty10",
                        "mesutozil" : "gunner8"
        }

        user_name = str(input("\nPlease enter your username: "))
        user_password = str(input("Enter your password: "))


        if user_name in existing_user_logins and user_password == existing_user_logins[user_name]:
            print("\033[94m\nLOGIN SUCCESSFUL, WELCOME ABOARD!\033[0m")
            #User is logged in, userinterface function to be displayed now with options
            user_interface(user_name) #Function call
            break

        else:
            print("\033[91m\nINVALID USERNAME OR PASSWORD; PLEASE PROVIDE A VALID ENTRY!\033[0m")



#Dealing with admin (option 2)
def admin_login():


    while True:

        existing_admin_logins = {"admin" : "password123"}
        

        admin_name = str(input("\nPlease enter your username: "))
        admin_password = str(input("Enter your password: "))


        if admin_name in existing_admin_logins and admin_password == existing_admin_logins[admin_name]:
            print("\033[94m\nLOGIN SUCCESSFUL, WELCOME ABOARD ADMIN!\033[0m")
            
            #Admin is logged in, admininterface function to be displayed now with options
            admin_interface(admin_name) #Function call

            break


        else:
            print("\033[91m\nINVALID USERNAME OR PASSWORD; PLEASE PROVIDE A VALID ENTRY!\033[0m")


#COLOURED HEADINGS -- PROGRAM STARTS 

def colouredHeadings():
    print("\033[38;5;208mAIRPLANE MANAGEMENT SYSTEM\033[0m")
    print()
    print("\033[92mLOGIN PANEL!\033[0m")
    print()
    readFromFile(flightsDataFileName)

while True:
    colouredHeadings()
    print("\nLogin the application as a user or an admin.")
    selected_option = str(input("\nEnter 1 to access as a user, 2 to access as an admin. "))

    if selected_option == "1":
        user_login()
        print("\nReturning to the main menu...\n")


    elif selected_option == "2":
        admin_login()
        print("\nReturning to the main menu...\n")

    else:
        print("\nInvalid entry, please select only option 1 or 2.")
        
