import math

# Inputs
wheelDiameter_in = 27.5 # user must provide this value
clock_period_ms = 10
lastTime_ms = 100
currentTime_ms = 200

# Distance Constants
FEET_PER_MILE = 5280
INCHES_PER_MILE = FEET_PER_MILE * 12

# Time Constants
MINUTES_PER_HOUR = 60
SECONDS_PER_MINUTE = 60
MS_PER_SECOND = 1000
MS_PER_HOUR = MS_PER_SECOND * SECONDS_PER_MINUTE * MINUTES_PER_HOUR

# Determine distance per rotation of the wheel
wheelCircumference_in = wheelDiameter_in * math.pi
distPerRotation_in = wheelCircumference_in
distPerRotation_mi = distPerRotation_in / INCHES_PER_MILE
print(f"Distance per Rotation (in): {distPerRotation_in}")
print(f"Distance per Rotation (mi): {distPerRotation_mi}")

# Determine time between sensor readings
rotationTime_ms = currentTime_ms - lastTime_ms
print(f"Rotation Time (ms): {rotationTime_ms}")

# Calculate speed in miles per hour
speed_mph = distPerRotation_mi / (rotationTime_ms / MS_PER_HOUR)

# Quantify the error introduced into speed calculation based on the clock rate
speed_error = (distPerRotation_mi / ((rotationTime_ms - clock_period_ms) / MS_PER_HOUR)) - speed_mph
print(f"Speed (mph): {speed_mph - speed_error/2} +-{speed_error/2}")
