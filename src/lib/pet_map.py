import rospy

## class Map
#
# Map structure definition and functions
class PetMap():
    ## The constructor
    #  @param self The object pointer
    def __init__(self):
        # initialization of dimension and positions on the Map
        self.dimX = rospy.get_param("map_dimension_x")
        self.dimY = rospy.get_param("map_dimension_y")
        self.homeX = rospy.get_param("home_x")
        self.homeY = rospy.get_param("home_y")
        self.actualX = self.homeX
        self.actualY = self.homeY

    ## method updateMap
    # @param x X position
    # @param y Y position
    def updateMap(self,x,y):
        self.actualX = x
        self.actualY = y


