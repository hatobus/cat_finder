import requests
import json


class ComputerVision():
    def __init__(self, APIKEY, URL):
        self.CPVISIONKEY = APIKEY
        self.CPVISIONURL = URL

    def getInfoPicture(self, fname):
        with open(fname, "rb") as f:
            bin = f.read()

        print(self.CPVISIONURL)

        headers = {
            "Content-Type" : "application/octet-stream",
            "Ocp-Apim-Subscription-Key": self.CPVISIONKEY
        }

        r = requests.post(self.CPVISIONURL, data=bin, headers=headers)

        res_json = r.json()
        # print(res_json["tags"])

        for tag in res_json["tags"]:
            # print(tag)
            if tag["name"] == "cat":
                return True

        return False
