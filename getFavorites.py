#!/usr/bin/python
# -*- coding: UTF-8 -*-

import plistlib
import os
import json

filePath = os.path.expanduser("~/Library/Application Support/DEVONthink 3/Favorites.plist")

if os.path.exists(filePath):
    result = {"items": []}
    plObjList = plistlib.readPlist(filePath)
    for plobj in plObjList:
        if type(plobj) != str:
            result["items"].append({
                "title": plobj["Name"],
                # "subtitle": "",
                "arg": plobj["UUID"]})
    print(json.dumps(result))
else:
    print('{"items": [{"title": "No Favorite Item","subtitle": "(*´･д･)?"}]}')
