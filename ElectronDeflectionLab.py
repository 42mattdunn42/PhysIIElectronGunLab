"""
This is a program to automatically calculate the initial velocity of an electron fired from an electron gun.
The required inputs are voltage, distance between plates, y-distance, and x-distance.
"""

# Given a string prompt, only returns the user input until a float is given
def get_user_input(prompt):
    try:
        return float(input(prompt))
    except:
        print("Please enter a float")
        return get_user_input(prompt)

# Calculates the initial velocity based off the voltage, plate distance, x distance, and y distance
def calc_veloc(voltage, x_dist, plate_dist, y_dist):

    electron_mass = 9.1 * 10 ** -31  # kg
    electron_charge = 1.6 * 10 ** -19  # C

    y_accel = (electron_charge * (voltage / plate_dist)) / electron_mass
    return x_dist / (((2 * y_accel * y_dist) ** 0.5) / y_accel)



# Get the distance between plates and y-distance as these will be constant for all voltages and x-distances

plate_dist = get_user_input("What is the distance between your plates in meters? ")

y_dist = get_user_input("What is the distance the electron travels in the y direction (meters)? ")

# Continually prompt the user to input new voltages and x-distances until they wish to stop.
# For every new volatge/distance, calculate the initial velocity

cont_flag = 'Y'

while cont_flag == 'Y':

    voltage = get_user_input("What is the current voltage between the plates (volts)? ")

    x_dist = get_user_input("What is the current distance the electron travels in the x direction (meters)? ")

    curr_veloc = calc_veloc(voltage, x_dist, plate_dist, y_dist)

    print(f"The initial x-velocity is {curr_veloc} m/s")
    print(f"That is {curr_veloc:e} m/s")

    cont_flag = input("Enter a new voltage and x-distance? (Y/N) ")[:1].upper()
