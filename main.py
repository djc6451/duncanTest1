#2d Case of point masses repelling one another
#2d Case of point masses repelling one another.
import math
import numpy
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
pointONEtheta = 0
pointTWOtheta = 1
pointONEr = 1
pointTWOr = 1
pointONEw = 2
pointTWOw = 2
pointONEa = 0
pointONEa = 0
damping = 0.05

#Distance Between the points
pointDistance = math.sqrt(   (pointONEr**2 + pointTWOr**2)   - 2*pointONEr*pointTWOr*math.cos(pointONEtheta-pointTWOtheta)     )
print("Starting Distance:" , pointDistance)


#Position Vectors for both point masses
positionVectorONE = numpy.array(     [     pointONEr * math.cos(pointONEtheta)     ,  pointONEr*math.sin(pointONEtheta)    ]             )
positionVectorTWO = numpy.array(       [    pointTWOr * math.cos(pointTWOtheta)     ,  pointTWOr*math.sin(pointTWOtheta)  ]           )

#Vector for the force direction , scaled by the inverse square distance between the points they are in opposite directions
forceONE = numpy.array(   [ pointONEr*math.cos(pointONEtheta) - pointTWOr*math.cos(pointTWOtheta) ,  pointONEr*math.sin(pointONEtheta) - pointTWOr*math.sin(pointTWOtheta)     ]   ) * (1/(pointDistance**2))
forceTWO = numpy.array(   [ pointONEr*math.cos(pointTWOtheta) - pointTWOr*math.cos(pointONEtheta) ,  pointONEr*math.sin(pointTWOtheta) - pointTWOr*math.sin(pointONEtheta)   ]   ) * (1/(pointDistance**2))

#Angle between the force vector and the position vector
angleONE = numpy.acos(   numpy.dot(positionVectorONE,forceONE)  / (numpy.linalg.norm(positionVectorONE) * numpy.linalg.norm(forceONE)) )
angleTWO = numpy.acos(   numpy.dot(positionVectorTWO,forceTWO)  / (numpy.linalg.norm(positionVectorTWO) * numpy.linalg.norm(forceTWO)) )
print("angle between force and vector", angleONE)

#Amount torque depends on orthogonality of force and position Vector
torqueONE = numpy.linalg.norm(positionVectorONE) * numpy.linalg.norm(forceONE) * math.sin(angleONE)
torqueTWO = numpy.linalg.norm(positionVectorTWO) * numpy.linalg.norm(forceTWO) * math.sin(angleTWO)
print("torque magnitude one" , torqueONE)
print("torque magnitude two" , torqueTWO)  # these two values should be the same, but their directions are equal and opposite.

oneX = []
oneY = []
twoX = []
twoY = []
oneAngularVelocities = []
twoAngularVelocities = []


# TO determine which direction the force should be in for each point mass
# this method calculates the Z component of the cross product as it is the value that is in opposite directions even though the
# magnitude of the forces is the same
def crossNegative(vectorONE , vectorTWO):
    if vectorONE[0]*vectorTWO[1]  - vectorONE[1]*vectorTWO[0]  > 0 :
        return 1
    if vectorONE[0]*vectorTWO[1]  - vectorONE[1]*vectorTWO[0] < 0:
        return -1



simulationLength = 500
for t in range(simulationLength):


    #I am multiplying by 0.1 because for the units to work out you have to multiply by time.
    #For example velocity  + acceleration*time works, but I can't just add the acceleration
    pointONEtheta += pointONEw * 0.1
    pointTWOtheta += pointTWOw * 0.1





    pointONEw +=   crossNegative(positionVectorONE, forceONE) * numpy.linalg.norm(torqueONE)*  0.1  - (pointONEw*0.05)
    pointTWOw += crossNegative( positionVectorTWO  , forceTWO) *  numpy.linalg.norm(torqueTWO)* 0.1  - (pointTWOw*0.05)

    #recalculate everything
    pointDistance = math.sqrt(
        (pointONEr ** 2 + pointTWOr ** 2) - 2 * pointONEr * pointTWOr * math.cos(pointONEtheta - pointTWOtheta))
    #print("Starting Distance:", pointDistance)

    # Position Vectors for both point masses
    positionVectorONE = numpy.array([pointONEr * math.cos(pointONEtheta), pointONEr * math.sin(pointONEtheta)])
    positionVectorTWO = numpy.array([pointTWOr * math.cos(pointTWOtheta), pointTWOr * math.sin(pointTWOtheta)])

    # Vector for the force direction , scaled by the inverse square distance between the points they are in opposite directions
    forceONE = numpy.array([pointONEr * math.cos(pointONEtheta) - pointTWOr * math.cos(pointTWOtheta),
                            pointONEr * math.sin(pointONEtheta) - pointTWOr * math.sin(pointTWOtheta)]) * (1 / (pointDistance ** 2))
    forceTWO = numpy.array([pointONEr * math.cos(pointTWOtheta) - pointTWOr * math.cos(pointONEtheta),
                            pointONEr * math.sin(pointTWOtheta) - pointTWOr * math.sin(pointONEtheta)]) * (1 / (pointDistance ** 2))

    # Angle between the force vector and the position vector
    angleONE = numpy.acos( numpy.dot(positionVectorONE, forceONE) / (numpy.linalg.norm(positionVectorONE) * numpy.linalg.norm(forceONE)))
    angleTWO = numpy.acos( numpy.dot(positionVectorTWO, forceTWO) / (numpy.linalg.norm(positionVectorTWO) * numpy.linalg.norm(forceTWO)))
    #print("angle between force and vector", angleONE)

    # Amount torque depends on angle between force and position Vector
    torqueONE = numpy.linalg.norm(positionVectorONE) * numpy.linalg.norm(forceONE) * math.sin(angleONE)
    torqueTWO = numpy.linalg.norm(positionVectorTWO) * numpy.linalg.norm(forceTWO) * math.sin(angleTWO)
    #print("torque magnitude one", torqueONE)
    #print("torque magnitude two", torqueTWO)  # these two values should be the same, but their directions are equal and opposite.

    oneX.append(  pointONEr*math.cos(pointONEtheta))
    oneY.append(  pointONEr*math.sin(pointONEtheta))
    twoX.append(pointTWOr * math.cos(pointTWOtheta))
    twoY.append( pointTWOr* math.sin(pointTWOtheta))
    oneAngularVelocities.append( pointONEw)
    twoAngularVelocities.append( pointTWOw)

    #print( "Point One W:", pointONEw , "    Point Two W" , pointTWOw )




#Plotting

fig, ax = plt.subplots()
ax.set_aspect('equal')
ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)

red_points, = ax.plot([], [], 'ro', markersize=5)
blue_points, = ax.plot([], [], 'bo', markersize=5)

ax.set_title("Updating Points")

#rect1 = plt.bar(1, oneAngularVelocities  , width = 0.5  , align='edge')
#rect2 = plt.bar( 2 , twoAngularVelocities , width = 0.5 ,  align='center')
# Loop to update the plot
for i in range(simulationLength):


    max_points = 1
    start_index = max(0, i - max_points + 1)

    # Update data for the points
    red_points.set_data(oneX[start_index:i + 1], oneY[start_index:i + 1])
    blue_points.set_data(twoX[start_index:i + 1], twoY[start_index:i + 1])

    #Plot the velocities on a bar graph




    plt.draw()  # Redraw the figure
    plt.pause(0.1)  # Pause for a brief moment


plt.show()