# Initial message
print("You're sleeping in your self driving tesla when you suddenly wake up and notice a traffic light ahead")
# Gets user input
trafficlightColour = input("What colour is the traffic light up ahead?: ").lower()
distanceToLight = float(input("How far is your car from the light?: "))
speedOfCar = float(input("How fast is the car going?: "))
timeToLight = distanceToLight/speedOfCar

# Determines whether the car should cross the light or not
if (trafficlightColour == "green") or (trafficlightColour == "yellow" and timeToLight >= 5 ) or (trafficlightColour == "red" and timeToLight >=2):
    print("teslaCommand.go()")
else:
    print("teslaCommand.stop()")