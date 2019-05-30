from environ import settings
from streetview import viewGetter

class CatFinder():
    def __init__(self):
        self.REQUESTURL = settings.REQUESTURL
        self.STREETVIEWAPIKEY = settings.STREETVIEWAPIKEY 
        self.COMPUTERVISIONKEY =  settings.COMPUTERVISIONKEY
        self.ViewGetter = viewGetter.viewGetter(self.STREETVIEWAPIKEY, self.REQUESTURL)

    def GetPicture(self):
        self.ViewGetter.getRandomPicture()


if __name__ == "__main__":
    CF = CatFinder()
    CF.GetPicture()