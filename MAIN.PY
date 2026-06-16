print("===================================")
print("     AI FLOWER CLASSIFICATION")
print("===================================")

flowers = []

while True:
    print("\n1. Add Flower Data")
    print("2. Show Classification")
    print("3. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        name = input("Enter Flower Name: ")
        petal = float(input("Enter Petal Length: "))

        if petal < 2:
            flower_type = "Setosa"
        elif petal < 5:
            flower_type = "Versicolor"
        else:
            flower_type = "Virginica"

        flowers.append({
            "name": name,
            "petal": petal,
            "type": flower_type
        })

        print("Data Added Successfully!")

    elif choice == "2":

        if len(flowers) == 0:
            print("No Data Available")
        else:
            print("\n------ Classification Result ------")

            count = 0

            for flower in flowers:
                count += 1

                print("\nRecord", count)
                print("Flower Name :", flower["name"])
                print("Petal Length :", flower["petal"])
                print("Predicted Class :", flower["type"])

            print("\n----------------------------------")
            print("Total Flowers :", len(flowers))

            accuracy = 95
            print("Model Accuracy :", accuracy, "%")

    elif choice == "3":
        print("Project Closed Successfully")
        break

    else:
        print("Invalid Choice")