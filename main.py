from pystyle          import *
from json             import load
from os               import system, name
from random           import randint
from threading        import Thread, Lock
from requests         import post, get
from urllib.parse     import urlencode
from utils.livecounts import livecounts
from utils.ttsign     import ttsign
from time             import time, sleep

class Tikreport:
    def __init__(self, *args, **kwargs):
        self.reasons   = ['9101', '91011', '9009', '90093', '90097', '90095', '90064', '90061', '90063', '9006', '9008', '90081', '90082', '9007', '1001', '1002', '1003', '1004', '9002', '90011', '90010', '9001', '9010', '9011', '90112', '90113', '9003', '90031', '90032', '90033', '90034', '90035', '90036', '9004', '9005', '9012', '910121', '910122', '91012', '91013', '910131', '910132', '910133', '910134', '910135', '91014', '9013', '9102']
        self.sessionid = load(open('config.json', 'r'))['sessionid']
        self.lock      = Lock()
        self.username  = ''
        self.count     = 0

    def __startup(self) -> None:
        system('cls' if name == 'nt' else 'clear')
        Thread(target = self.__title_loop).start()
        
        txt = '''\n\n   ▄▄▄▄▀ ▄█ █  █▀     █▄▄▄▄ ▄███▄   █ ▄▄  ████▄ █▄▄▄▄    ▄▄▄▄▀ \n▀▀▀ █    ██ █▄█       █  ▄▀ █▀   ▀  █   █ █   █ █  ▄▀ ▀▀▀ █    \n    █    ██ █▀▄       █▀▀▌  ██▄▄    █▀▀▀  █   █ █▀▀▌      █    \n   █     ▐█ █  █      █  █  █▄   ▄▀ █     ▀████ █  █     █     \n  ▀       ▐   █         █   ▀███▀    █            █     ▀      \n\n'''
        print(
            Colorate.Vertical(
                Colors.DynamicMIX((Col.light_blue, Col.purple)), Center.XCenter(txt)
            )
        )

    def __title_loop(self) -> None:
        if name == "nt":
            while True:
                system(f'title TikTok Report Bot by @xtekky ^| sessionid: {self.sessionid} ^| target: @{self.username} ^| reports: {self.count}')
                sleep(0.1)

    def __video_report(self, owner_id, object_id, reason) -> dict:
        try:
            params =  urlencode({
                "report_type" : "video",
                "object_id"   : object_id,
                "owner_id"    : owner_id,
                "isFirst"     : 1,
                "report_desc" : "",
                "uri"         : "",
                "reason"      : reason,
                "category"    : ""
            })

            report_req = post("https://api16-va.tiktokv.com/aweme/v1/aweme/feedback/?" + params, 
                headers = {
                "cookie"     : "store-idc=alisg; store-country-code=kr; store-country-code-src=did; sessionid=%s" % self.sessionid,
                "x-gorgon"   : "0",
                "x-khronos"  : str(int(time())),
                "host"       : "api16-va.tiktokv.com",
                "user-agent" : "okhttp/3.10.0.1"
            })

            if report_req.json()['status_code'] == 0:
                self.count += 1
                
                self.lock.acquire()
                print(
                    Colorate.Horizontal(
                        Colors.green_to_white, '            {x} - reported %s (%s) reason: %s' % (str(object_id),str(report_req.json()['log_pb']['impr_id']), str(reason))
                    )
                )
                self.lock.release()
                

        except Exception as e:
            pass
            
    def __account_report(self, username, reason) -> None:
        try:

            user_info    = livecounts.user_info(username)
            account_info = livecounts.account_info(self.sessionid)

            params = urlencode({
                "secUid"          : user_info['secUserId'],
                "target"          : user_info['userId'],
                "object_id"       : user_info['userId'],
                "owner_id"        : user_info['userId'],
                "reporter_id"     : account_info['user_id'],
                
                "aid"             : 1988,
                "app_language"    : "en",
                "app_name"        : "tiktok_web",
                "battery_info"    : "0.94",
                "browser_language": "en",
                "browser_name"    : "Mozilla",
                "browser_online"  : "true",
                "browser_platform": "Win32",
                "browser_version" : "5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36",
                "channel"         : "tiktok_web",
                "cookie_enabled"  : "true",
                "current_region"  : "DE",
                "device_id"       : randint(7000000000000000000, 8999999999999999999),
                "device_platform" : "web_pc",
                "focus_state"     : "true",
                "from_page"       : "user",
                "history_len"     : 4,
                "is_fullscreen"   : "false",
                "is_page_visible" : "true",
                "lang"            : "en",
                "nickname"        : user_info['name'],
                "os"              : "windows",
                "priority_region" : "IE",
                "reason"          : reason,
                "region"          : "DE",
                "report_type"     : "user",
                "screen_height"   : 864,
                "screen_width"    : 1536,
                "tz_name"         : "Europe/Paris",
                "webcast_language": "en",
                "msToken"         : "missing",
                "X-Bogus"         : None,
                "_signature"      : None
            })

            apiresponse = get('https://www.tiktok.com/aweme/v1/aweme/feedback/?' + params,
                headers = {
                    'authority' : 'www.tiktok.com',
                    'cookie'    : 'sessionid=%s' % self.sessionid,
                    'referer'   : 'https://www.tiktok.com/@allen_and_straypets',
                    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36',
            })
            
            self.count += 1
            
            self.lock.acquire()
            print(
                Colorate.Horizontal(
                    Colors.green_to_white, '            {x} - reported %s (%s) reason: %s' % (str(username),str(apiresponse.json()['log_pb']['impr_id']), str(reason))
                )
            )
            self.lock.release()

        except Exception as e:
            if self.lock.locked():self.lock.release()
            print(e)

    def __report_all_videos(self, username):
        user_info  = livecounts.user_info(username)
        max_cursor = 0

        while True:
            params = urlencode({
                "source"      : 0,
                "max_cursor"  : max_cursor,
                "sec_user_id" : user_info['secUserId'],
                "count"       : 33,
                
                "device_type"       : "SM-G988N",
                "app_name"          : "musically_go",
                "host_abi"          : "armeabi-v7a",
                "channel"           : "googleplay",
                "device_platform"   : "android",
                "iid"               : 7159249365869414149,
                "device_id"         : 6712029815367206401,
                "version_code"      : 160904,
                "device_brand"      : "samsung",
                "os_version"        : 9,
                "aid"               : 1340
            })

            response = get("https://api16-normal-c-alisg.tiktokv.com/aweme/v1/aweme/post/?" + params, 
                headers = {
                    **ttsign(params, None, None).get_value(),
                    "host"       : "api16-normal-c-alisg.tiktokv.com",
                    "user-agent" : "okhttp/3.10.0.1"
            })

            try:
                if response.json()["status_msg"] == "No more videos":
                    break

            except Exception:
                try:
                    max_cursor = response.json()["max_cursor"]

                except Exception:
                    break

            for vid in response.json()["aweme_list"]:
                for reason in self.reasons:
                    Thread(
                        target = self.__video_report, 
                        args   = [user_info['userId'], vid['aweme_id'], reason]).start()

            if response.json()['has_more'] == 0:
                break

        return

    def mainloop(self) -> None:
        self.__startup()
        
        username = str(Write.Input("            {?} - username > ", Colors.blue_to_purple, interval=0.001)); self.username = username
        mode     = str(Write.Input("            {?} - mode (account/videos) > ", Colors.blue_to_purple, interval=0.001))

        if mode == 'videos':
            print('\n'); self.__report_all_videos(username)
        else:
            print('\n')
            while True:
                for reason in self.reasons:
                    self.__account_report(username, reason)

if __name__ == "__main__":
    Tikreport(None).mainloop()