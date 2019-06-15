from environ import settings
from streetview import viewGetter
from cpvision import computervison

class CatFinder():
    def __init__(self):
        self.REQUESTURL = settings.REQUESTURL
        self.STREETVIEWAPIKEY = settings.STREETVIEWAPIKEY 
        self.COMPUTERVISIONKEY =  settings.COMPUTERVISIONKEY
        self.COMPUTERVISIONURL = settings.COMPUTERVISIONKEY
        self.ViewGetter = viewGetter.viewGetter(self.STREETVIEWAPIKEY, self.REQUESTURL)
        self.CPVISION = computervison.ComputerVision(self.COMPUTERVISIONURL, self.REQUESTURL)

    def GetPicture(self):
        isnew = self.ViewGetter.getRandomPicture()
        
        if len(isnew) == 0:
            print("invalid point")

        self.FindCat(isnew)

    def FindCat(self, fname):
        iscat = self.CPVISION.getInfoPicture(fname)
        if iscat:
            print("cat found")
            return 
        else:
            print("cat not found")


if __name__ == "__main__":
    CF = CatFinder()
    # CF.GetPicture()
    CF.FindCat("./pic/catimg/cattest.png")