import requests
from requests       import post
from urllib.parse   import urlencode
from time           import time

class Tikreport:
    def __init__(self, *args, **kwargs):
        pass
    
    def __video_report(self, owner_id, object_id, reason) -> dict:
        params =  urlencode({
            "report_type" : "video",
            "object_id"   : object_id,
            "owner_id"    : owner_id,
            "isFirst"     : 1,
            "report_desc" : "",
            "uri"         : "",
            "reason"      : 9005,
            "category"    : "",
        })
        
        return post("https://api16-va.tiktokv.com/aweme/v1/report/video/?%s" % params, 
            headers = {
            "cookie"     : "store-idc=alisg; store-country-code=kr; store-country-code-src=did;",
            "x-gorgon"   : "0",
            "x-khronos"  : str(int(time())),
            "host"       : "api16-va.tiktokv.com",
            "user-agent" : "okhttp/3.10.0.1"
        }).json()
