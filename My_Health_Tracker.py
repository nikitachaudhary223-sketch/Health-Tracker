print("=================")
print("My Health Tracker")
print("=================")

while True:
    print("1.Record Today's Health")
    print("2.View Today's Health")
    print("3.Track Water")
    print("4.Track Sleep")
    print("5.Track Excercise")
    print("6.Track Period")
    print("7.Health Summary")
    print("8.Exit")
    print("=================")

    choice=int(input("Enter what you want to check:"))

    if choice==1:
        print("Record Today's Health")
        sleep=float(input("How many hours did you sleep?"))
        water=float(input("How many glasses of water did you drink today?"))
        excercise=float(input("How many minutes did you excercise?"))
        energy=int(input("What is your energy level (1-10)?"))
        mood=int(input("What is your mood level (1-10)?"))

    elif choice==2:
        print("View Today's Health")
        print("====Today's Health====")
        print(f"Sleep: {sleep} hrs")
        print(f"Water: {water} glasses")
        print(f"Excercise: {excercise} minutes")
        print(f"Energy: {energy}/10")
        print(f"Mood: {mood}/10")
        print("=======================")

    elif choice==3:
        print("Let's Track how much water we drink today")
        water=int(input("Enter how many glasses of water you drink:"))
        if water>=8:
            print("It is good")
        elif water<6:
            print("Drink more")
        else:
            print("Drink water now")

    elif choice==4:
        print("Let's track our sleep cycle")
        sleep=float(input("How many hours did you sleep?"))
        if sleep>=8:
            print("Good sleep")
        elif sleep<6:
             print("You need more sleep")
        else:
            print("Try to sleep a little more")
        
    elif choice==5:
        print("Let's track our excersise session")
        excercise=float(input("How many minutes did you excercise?"))
        if excercise>=30:
            print("Great job!")
        elif excercise<15:
            print("Try to move more today")
        else:
            print("Good,but you can do a little more")        

    elif choice==6:
        print("Let's track our period cycle")
        period=(input("Are you on your period today?(yes/no):"))

        if period=="yes":
            print("Period recorded for today")
        elif period=="no":
            print("No period recorded today")
        else:
            print("Please enter yes or no")


    elif choice==7:
        print("Let's see our health summary")
        print("*******Health Summary*******")
        print(f"Sleep: {sleep} hrs")
        print(f"Water: {water} glasses")
        print(f"Excercise: {excercise} minutes")
        print(f"Energy: {energy}/10")
        print(f"Mood: {mood}/10")
        print("******************************")
        

    elif choice==8:
        print("View again and hustle everyday")
        break

    else:
        print("Invalid option")
