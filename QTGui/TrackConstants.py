class TrackConstants():
    def __init__(self):
        
        self.steps  = 16500
        self.length = 0.22                   # [m]
        self.dx     = self.length/self.steps # [m]
        
    def printinfo(self):
        
        print("------------ Track metrics -------------")
        print("Maximum number of steps : steps  = " + str(self.steps))
        print("Track length            : length = " + str(self.length))
        print("Distance per step       : dx     = " + str(self.dx))
        