# Initial message
print("Welcome to the traffic light simulator.\nYour are at an intersection where there is a traffic light.")
# Gets user input
trafficlightColour = input("What colour is the traffic light up ahead?: ").lower()
# if the light is green, rest of the inputs and calulations are not needed
if (trafficlightColour != "green"):
    distanceToLight = float(input("How far is your car from the light?(m): "))
    speedOfCar = float(input("How fast is the car going?(m/s): "))
    timeToLight = distanceToLight/speedOfCar
    # Determines whether the car should cross the light or not
    if(trafficlightColour == "yellow" and timeToLight <= 5) or (trafficlightColour == "red" and timeToLight <=2):
        print("Go.")
    else:
        print("Stop.")
else:
    print("Go.")
