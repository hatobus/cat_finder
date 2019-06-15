from environ import settings
from streetview import viewGetter
from cpvision import computervison

import os

class CatFinder():
    def __init__(self):
        self.REQUESTURL = settings.REQUESTURL
        self.STREETVIEWAPIKEY = settings.STREETVIEWAPIKEY 
        self.COMPUTERVISIONKEY =  settings.COMPUTERVISIONKEY
        self.COMPUTERVISIONURL = settings.COMPUTERVISIONURL
        self.ViewGetter = viewGetter.viewGetter(self.STREETVIEWAPIKEY, self.REQUESTURL)
        self.CPVISION = computervison.ComputerVision(self.COMPUTERVISIONKEY, self.COMPUTERVISIONURL)

    def GetPicture(self):
        isnew = self.ViewGetter.getRandomPicture()
        
        if len(isnew) == 0:
            print("invalid point")
            return False

        self.FindCat(isnew)

    def FindCat(self, fname):
        iscat = self.CPVISION.getInfoPicture(fname)
        if iscat:
            print("cat found")
            return 
        else:
            print("cat not found")
            os.remove(fname)


if __name__ == "__main__":
    CF = CatFinder()
    CF.GetPicture()