print("====================================")
print("      AI RECOMMENDATION SYSTEM")
print("====================================")

name = input("Enter Your Name: ")

print("\nHello", name)

while True:

    print("\nSelect Your Interest")
    print("1. Movies")
    print("2. Music")
    print("3. Sports")
    print("4. Books")
    print("5. Technology")
    print("6. Exit")

    choice = input("\nEnter Choice: ")

    if choice == "1":

        print("\nMovie Recommendations")
        print("---------------------")
        print("1. Avengers")
        print("2. Interstellar")
        print("3. Inception")
        print("4. The Dark Knight")
        print("5. Spider-Man")

    elif choice == "2":

        print("\nMusic Recommendations")
        print("---------------------")
        print("1. Believer")
        print("2. Shape Of You")
        print("3. Perfect")
        print("4. Faded")
        print("5. Thunder")

    elif choice == "3":

        print("\nSports Recommendations")
        print("----------------------")
        print("1. Cricket")
        print("2. Football")
        print("3. Badminton")
        print("4. Volleyball")
        print("5. Tennis")

    elif choice == "4":

        print("\nBook Recommendations")
        print("--------------------")
        print("1. Rich Dad Poor Dad")
        print("2. Atomic Habits")
        print("3. Think And Grow Rich")
        print("4. Ikigai")
        print("5. The Alchemist")

    elif choice == "5":

        print("\nTechnology Recommendations")
        print("--------------------------")
        print("1. Python")
        print("2. Artificial Intelligence")
        print("3. Machine Learning")
        print("4. Data Science")
        print("5. Web Development")

    elif choice == "6":

        print("\n================================")
        print("Thank You For Using Our System")
        print("================================")
        break

    else:

        print("\nInvalid Choice")

    feedback = input("\nDid you like the recommendations? (yes/no): ")

    if feedback.lower() == "yes":
        print("Great! Happy Learning.")
    else:
        print("We will improve our recommendations.")

print("\nProject Completed Successfully")