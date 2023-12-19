class Protected:
    def __init__(self):
        self.__privatevar = 20

    def getprivate(self):
        print(self.__privatevar)

    def setprivate(self, private):
        self.__privatevar = private


obj = Protected()
obj.getprivate()
obj.setprivate(11)
obj.getprivate()

#Obj gets the data of the private variable

#the output should be 20, 11
