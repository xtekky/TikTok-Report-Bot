from re             impo
from hashlib        import sha256
from threading      import Thread, active_count
from requests       import post, get
from urllib.parse   import urlencode
from time           import time

class Livecounts:
    @staticmethod
    def __signature(timestamp) -> dict:
        x_aurora = str(3 * timestamp)
        x_joey   = str(timestamp)
        x_maven  = sha256(f"0AVwElhWi1IfwcZKSNzq7E^84hFQ4ykenNAxeY7r@6ho1oTd6Ug*!WC&p$2aGY8MLHEkH0i8XCwnj3#JqI1NzCb91$gNzLYCbbG@NqvQMbcf8W9v3%s#uzjP@z*!e9a41JNWBqRIMJ*ULuav5k8z4kBj2^BCC%!3q@N0zZOS^TL#GzVz@9fhjg&^mSWi&oU5GMoCu9{timestamp}".encode()).hexdigest()
        x_midas  = sha256(str(timestamp + 64).encode()).hexdigest()
        
        return {
            'x-aurora' : x_aurora,
            'x-joey'   : x_joey,
            'x-maven'  : x_maven,
            'x-mayhem' : "553246736447566b58312f7a4f72413653425342717a6e4231596f7a4d59686564764842324b396478544443756669734d56706f4346334633456366724b6732",
            'x-midas'  : x_midas,
        }
    
    @staticmethod
    def video_info(video_id) -> dict:
        timestamp = int(time() * 1000)
        
        headers = {
            **Livecounts.__signature(timestamp),
            'authority' : 'tiktok.livecounts.io',
            'origin'    : 'https://livecounts.io',
            'referer'   : 'https://livecounts.io/',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36',
        }
        
        req = get(f'https://tiktok.livecounts.io/video/data/{video_id}', headers=headers)
        
        return req.json()['author']['userId']

class Tikreport:
    def __init__(self, *args, **kwargs):
        self.reasons = ['9101', '91011', '9009', '90093', '90097', '90095', '90064', '90061', '90063', '9006', '9008', '90081', '90082', '9007', '1001', '1002', '1003', '1004', '9002', '90011', '90010', '9001', '9010', '9011', '90112', '90113', '9003', '90031', '90032', '90033', '90034', '90035', '90036', '9004', '9005', '9012', '910121', '910122', '91012', '91013', '910131', '910132', '910133', '910134', '910135', '91014', '9013', '9102']
        self.index   = 0
        
    def __video_report(self, owner_id, object_id, reason) -> dict:
        params =  urlencode({
            "report_type" : "video",
            "object_id"   : object_id,
            "owner_id"    : owner_id,
            "isFirst"     : 1,
            "report_desc" : "",
            "uri"         : "",
            "reason"      : reason,
            "category"    : "",
        })

        if post("https://api16-va.tiktokv.com/aweme/v1/aweme/feedback/?" + params, 
            headers = {
            "cookie"     : "store-idc=alisg; store-country-code=kr; store-country-code-src=did;",
            "x-gorgon"   : "0",
            "x-khronos"  : str(int(time())),
            "host"       : "api16-va.tiktokv.com",
            "user-agent" : "okhttp/3.10.0.1"}).json()['status_code'] == 0:
            
            print('{x} - reported %s reason: %s' % (str(object_id), str(reason)))
        
    def mainloop(self) -> None:
        link = input('Video link: ')
        object_id = str(
            re.findall(r"(\d{18,19})", link)[0]
            if len(re.findall(r"(\d{18,19})", link)) == 1
            else re.findall(
                r"(\d{18,19})",
                requests.head(link, allow_redirects=True, timeout=5).url
            )[0]
        )
        
        
        owner_id  = Livecounts.video_info(object_id)
        
        while self.index < len(self.reasons):
            if active_count() < 10:
                Thread(target = self.__video_report, args = [owner_id, object_id, self.reasons[self.index]]).start()
                self.index += 1
            

if __name__ == "__main__":
    Tikreport().mainloop()