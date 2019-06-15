import urllib
import json


class ComputerVision():
    def __init__(self, APIKEY, URL):
        self.CPVISIONKEY = APIKEY
        self.CPVISIONURL = URL

    def getInfoPicture(self, fname):
        with open(fname, "rb") as f:
            bin = f.read()

        print(self.CPVISIONURL)

        req = urllib.request.Request(self.CPVISIONURL)
        req.add_header("Content-Type", "application/octet-stream")
        req.add_header("Ocp-Apim-Subscription-Key", self.CPVISIONKEY)

        with urllib.request.urlopen(req, data=bin) as res:
            print(res.getcode())
            print(res.body().decode("utf-8"))
            tags = json.load(res)

        print(tags["tags"])

        for tag in tags["tags"]:
            if tag["name"] == "cat":
                print("cat found")
                return True

        print("cat not found")
        return False
