started = False

while True:
    command = input('> ').lower()
    if command == "start":
        if started:
            print("Car is already started. Stop the car!")
        else:
            started = True
            print('Car started... Ready to go!')
    elif command == "stop":
        if not started:
            print("Car is already stopped. Start the car!")
        else:
            started = False
            print('Car stopped.')
    elif command == "help":
        print("""
start --> to start the car
stop --> to stop the car
quit --> to exit
        """)
    elif command == "quit":
        break
    else:
        print("I don't understand...")
