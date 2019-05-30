import random
import urllib
import urllib.request
import os
from os.path import join, dirname
from dotenv import load_dotenv
import time

from PIL import Image


class viewGetter():
    def __init__(self, APIKEY, URL):
        self.SVAPIKEY = APIKEY
        self.SVURL = URL

    def getRandomPicture(self):
        # 20回ランダムに座標を取得して、画像が返ってくるかで見る
        for n in range(1):
            # 経度
            longtitude = str(random.uniform(127, 145))
            # 緯度
            latitude = str(random.uniform(26, 45))

            size = "640x640"

            url = self.SVURL + "?location=" + latitude + "," + longtitude + "&size=" + size + "&key=" + self.SVAPIKEY
            print(url)

            req = urllib.request.Request(url)
            with urllib.request.urlopen(req) as res:
                print(res.getcode())
                rawpic = res.read()

            isdiff = self.picComp(rawpic)

            if isdiff == True:
                now = int(time.time())
                jpgfile = "Cat" + now + ".jpeg"
                with open(".pic/catimg/"+jpgfile, "wb") as rp:
                    rp.write(rawpic)


    def picComp(self, rawimg):
        fname = "./pic/notfound/streetviewnotfound.jpeg"
        with open(fname, 'rb') as img:
            notfoundimg = img.read()

        if rawimg == notfoundimg:
            print("same as notfound")
            return False
        else:
            return True
            