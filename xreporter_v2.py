import requests, json, threading, random


class Reporter:
    def __init__(self):
        self.username = input(' [ ? ] Username: ')
        self.reason = "317" #underage ~ 13
        self.report_count = 0
        self.threads = int(input(' [ ? ] Threads: '))

        self.user_id  = ""
        self.secuid  = ""

        self.getinfo()

    def getinfo(self):
        HEAD = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:99.0) Gecko/20100101 Firefox/99.0",
        "Cookie": "msToken=zgbEqIjfSC7M7QdTTpHDkpWLtnY4JnK22HiSE1iHCRGBBYY_36Gm-gMDqyGLBjpPE2svzjVPNGWyMFYUUEBwmGkr5y2qQuKmfjfTh0i2hfOsb_B7jfDrbd9a4IhjMLPyUIRNIZLqzG6PldNNXA=="
        }
        url = f"https://www.tiktok.com/api/user/detail/?device_id=7098862702289995269&uniqueId={self.username}"
        DATA = requests.get(url, headers=HEAD).json()["userInfo"]["user"]

        self.user_id = DATA["id"]
        self.username = DATA["uniqueId"]
        self.secuid = DATA["secUid"]

        for _ in range(self.threads):
            threading.Thread(target=self.report()).start()


    def report(self):
        while True:
            head =  {
                "user-agent": "Mozilla/5.0 (Linux; U; Android 4.4.2; en-us; SCH-I535 Build/KOT49H) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30"
            }

            if "Thanks for your feedback" in requests.get(f'https://www.tiktok.com/aweme/v1/aweme/feedback/?aid=1988&app_language=TK&channel=tiktok_web&current_region=TK&device_id={random.randint(1000000000000000000, 9999999999999999999)}&lang=en&nickname={self.username}&object_id=76493735542&os=onlp&owner_id={self.user_id}&reason={self.reason}&region=TK&report_type=user&secUid={self.secuid}&target={self.user_id}&tz_name=Tekky%2FOnlp', headers=head).text:
                self.report_count += 1
                print(f' [ * ] Reported {self.report_count} times')
            else:
                print(' [ * ] Failed to report')


if __name__ == '__main__':
    Reporter()
