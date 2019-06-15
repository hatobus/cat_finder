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
        for n in range(20):
            # 経度
            longtitude = str(round(random.uniform(127, 145), 6))
            # 緯度
            latitude = str(round(random.uniform(26, 45), 6))

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
                jpgfile = ".pic/catimg/" + "Cat" + now + ".jpeg"
                with open(jpgfile, "wb") as rp:
                    rp.write(rawpic)
                return jpgfile

        return ""


    def picComp(self, rawimg):
        # 指定した場所にストリートビューの画像がない場合
        # 帰ってくる画像が同じになるのでそれを比較する。
        fname = "./pic/notfound/streetviewnotfound.jpeg"
        with open(fname, 'rb') as img:
            notfoundimg = img.read()

        if rawimg == notfoundimg:
            print("same as notfound")
            return False
        else:
            return True
            