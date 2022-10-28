from hashlib    import sha256
from requests   import get
from time       import time
from json       import loads
from re         import findall

class livecounts:
    @staticmethod
    def __signature(timestamp: int) -> dict:
        
        return {
            'x-aurora' : str(3 * timestamp),
            'x-joey'   : str(timestamp),
            'x-maven'  : sha256(f"0AVwElhWi1IfwcZKSNzq7E^84hFQ4ykenNAxeY7r@6ho1oTd6Ug*!WC&p$2aGY8MLHEkH0i8XCwnj3#JqI1NzCb91$gNzLYCbbG@NqvQMbcf8W9v3%s#uzjP@z*!e9a41JNWBqRIMJ*ULuav5k8z4kBj2^BCC%!3q@N0zZOS^TL#GzVz@9fhjg&^mSWi&oU5GMoCu9{timestamp}".encode()).hexdigest(),
            'x-mayhem' : "553246736447566b58312f7a4f72413653425342717a6e4231596f7a4d59686564764842324b396478544443756669734d56706f4346334633456366724b6732",
            'x-midas'  : sha256(str(timestamp + 64).encode()).hexdigest()
        }
    
    @staticmethod
    def video_info(video_id: (int or str)) -> dict:
        timestamp = int(time() * 1000)
        
        headers = {
            **livecounts.__signature(timestamp),
            'authority' : 'tiktok.livecounts.io',
            'origin'    : 'https://livecounts.io',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36',
        }
        
        req = get(f'https://tiktok.livecounts.io/video/data/{video_id}', headers=headers)
        
        return req.json()['author']['userId']
    
    @staticmethod
    def user_info(username: str) -> dict:
        html_data   = get(f'https://livecounts.io/tiktok-live-follower-counter/{username}').text
        parsed_info = loads(findall(r'n">(.*)<\/s', html_data)[0])
        
        return parsed_info['props']['pageProps']['data']
    
    @staticmethod
    def account_info(sessionid: str) -> dict:
        return get('https://www.tiktok.com/passport/web/account/info/?aid=1459&app_language=en&app_name=tiktok_web',
            headers  = {
            'authority' : 'www.tiktok.com',
            'cookie'    : f'sessionid={sessionid}',
            'referer'   : 'https://www.tiktok.com/',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36',
        }).json()['data']
