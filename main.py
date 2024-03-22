# Name - Krisha Hemani
#      - Justin Ha
# Program - Practice
# Date - 02/22/2024
# Module 4 - Rolodex Menu
# Purpose - Create the program that allow you view, read, search, and modify the contact list which is made up for the conatct information.

import contact
import check_input


def read_file():
  file = open("addresses.txt", "r")
  contacts = []
  for line in file:
    data = line.strip().split(',')
    info = contact.Contact(data[0], data[1], data[2], data[3], data[4],
                           data[5])
    contacts.append(info)
  return sorted(contacts)


def write_file(contacts):
  with open("addresses.txt", "w") as file:
    for contact in contacts:
      file.write(repr(contact) + "\n")


def get_menu_choice():
  """The menu of the program"""
  print(
      "\nRolodex Menu:\n1. Display Contacts\n2. Add Contact\n3. Search Contacts\n4. Modify Contact\n5. Save and Quit"
  )
  return check_input.get_int_range("> ", 1, 5)


def modify_contact(con):
  """ the contact to modify """
  print(con)
  while True:
    print("\nModify Menu:")
    print("1. First name")
    print("2. Last name")
    print("3. Phone")
    print("4. Address")
    print("5. City")
    print("6. Zip")
    print("7. Save")
    choice = check_input.get_int_range("> ", 1, 7)
    if choice == 7:
      break
    elif choice == 1:
      con.firstname = input("Enter first name: ")
    elif choice == 2:
      con.lastname = input("Enter last name: ")
    elif choice == 3:
      con.phone = input("Enter phone #: ")
    elif choice == 4:
      con.address = input("Enter address: ")
    elif choice == 5:
      con.city = input("Enter city: ")
    elif choice == 6:
      con.zip = input("Enter zip: ")
  return con


def main():
  """The main fuction to run of the program"""
  contacts = read_file()
  while True:
    choice = get_menu_choice()

    if choice == 1:  # Display Contacts
      print("Number of contacts:", len(contacts))
      for idx, con in enumerate(contacts, 1):
        print()
        print(f"{idx}. {con}")
    elif choice == 2:  # Add Contact
      print("Enter the new contact")
      first_name = input("Enter first name: ")  #first name
      last_name = input("Enter last name: ")  #last name
      phone = input("Enter phone #: ")  #phone number
      address = input("Enter address: ")  #address
      city = input("Enter city: ")  #city
      zip = input("Enter zip: ")  #zip
      new_contact = contact.Contact(first_name, last_name, phone, address,
                                    city, zip)
      contacts.append(new_contact)
      contacts.sort()
    elif choice == 3:  #search contact
      print("Search by:")
      print(f"1. Search by last name")
      print(f"2. Search by zip code")
      search_choice = check_input.get_int_range("> ", 1, 2)
      if search_choice == 1:
        last_name = input("Enter last name: ")
        for con in contacts:
          if con.lastname == last_name:
            print()
            print(con)
      else:
        search_term = input("Enter zip code: ")
        matches = [
            contact for contact in contacts if contact.zip == search_term
        ]
        if matches:
          for idx, match in enumerate(matches, 1):
            print(f"{idx}. {match}")
        else:
          print("No contacts found.")
    elif choice == 4:  #modify contact
      search_first_name = input("Enter first name: ")
      search_last_name = input("Enter last name: ")
      print()
      for con in contacts:
        if con.firstname == search_first_name and con.lastname == search_last_name:
          modified_con = modify_contact(con)
          index = contacts.index(con)
          contacts[index] = modified_con
    elif choice == 5:  #Save and Quit
      write_file(contacts)
      print("Saving File...\nEnding Program")
      break


main()
