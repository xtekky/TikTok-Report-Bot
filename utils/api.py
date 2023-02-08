from base64        import b64decode, b64encode
from Crypto.Cipher import AES
from socket        import socket, AF_INET, SOCK_STREAM
from json          import loads
from urllib.parse  import quote, urlencode
from random        import randint
from tls_client    import Session, response
from execjs        import compile


class Api:
    def __init__(this, userAgent: str = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36', cookies: dict = {}):
        this.cookies    = cookies
        this.userAgent  = userAgent
        this.client     = Session(client_identifier='chrome_109')
        this.signer     = compile(bytes.fromhex(open('./utils/jsvmp.hex').read()[::-1]).decode())
    
    @staticmethod
    def x_tt_decrypt(enc: bytes | str, key: bytes = b"webapp1.0+202106") -> str:
        return (
            AES.new(key, AES.MODE_CBC, key)
                .decrypt(b64decode(enc))
                .strip()
                .decode("utf-8")
        )

    @staticmethod
    def x_tt_encrypt(params: str, key: bytes = b"webapp1.0+202106") -> str:
        params = f"{params}&is_encryption=1".encode("utf-8")

        return (
            b64encode(
                AES.new(key, AES.MODE_CBC, key).encrypt(params + bytes([(16 - (len(params) % 16))]) * (16 - (len(params) % 16))))
                .decode("utf-8")
        )
    
    def sign(this, params: str, ua: str) -> str: #, host: str = 'localhost', port: int = 3000
        
        return params + '&X-Bogus=' + this.signer.call('sign', params, ua)
        
        # with socket(AF_INET, SOCK_STREAM) as s:
        #     s.connect((host, port))
        #     s.sendall(f"GET /?url={quote(f'https://www.tiktok.com/?{params}')}&user_agent={quote(ua)} HTTP/1.0\r\n\r\n".encode())
        #     response = s.recv(2048)
        
        # return loads(response.split(b'\r\n')[-1])['signed_url'].split('?')[1]
    
    def get_params(this, extra: dict = {}, device_id: int = randint(7000000000000000000, 7999999999999999999)) -> str:
        return urlencode({
            **extra,
            'aid'               : 1988,
            'app_language'      : 'en',
            'app_name'          : 'tiktok_web',
            'battery_info'      : 1,
            'browser_language'  : 'en',
            'browser_name'      : 'Mozilla',
            'browser_online'    : 'true',
            'browser_platform'  : 'Win32',
            'browser_version'   : this.userAgent,
            'channel'           : 'tiktok_web',
            'cookie_enabled'    : 'true',
            'device_id'         : device_id,
            'device_platform'   : 'web_pc',
            'focus_state'       : 'true',
            'from_page'         : 'user',
            'history_len'       : '3',
            'is_fullscreen'     : 'false',
            'is_page_visible'   : 'true',
            'os'                : 'windows',
            'priority_region'   : 'FR',
            'referer'           : '',
            'region'            : 'FR',
            'screen_height'     : '1080',
            'screen_width'      : '1920',
            'tz_name'           : 'Africa/Casablanca',
            'webcast_language'  : 'en',
        })
    
    def get_headers(this, extra: dict = {}) -> dict:
        return {
            **extra,
            'authority'          : 'www.tiktok.com',
            'accept'             : '*/*',
            'accept-language'    : 'en,fr-FR;q=0.9,fr;q=0.8,es-ES;q=0.7,es;q=0.6,en-US;q=0.5,am;q=0.4,de;q=0.3',
            'referer'            : 'https://www.tiktok.com/',
            'sec-ch-ua'          : '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"',
            'sec-ch-ua-mobile'   : '?0',
            'sec-ch-ua-platform' : '"Windows"',
            'sec-fetch-dest' : 'empty',
            'sec-fetch-mode' : 'cors',
            'sec-fetch-site' : 'same-origin',
            'cookie'         : this.cookies,
            'user-agent'     : this.userAgent
        }
    
    def user_videos(this, secUid: str, count: int = 1, cursor: int = 0) -> response:
        params = this.get_params({
            'secUid': secUid,
            # 'userId': userId,
            'count' : count,
            'cursor': cursor 
        })

        return this.client.get(f'https://www.tiktok.com/api/post/item_list/?{this.sign(params, this.userAgent)}', headers = this.get_headers(), cookies = this.cookies)
    
    def user_info(this, uniqueId: str) -> response:
        params = this.get_params({
            'uniqueId': uniqueId
        })

        return this.client.get(f'https://www.tiktok.com/api/user/detail/?{this.sign(params, this.userAgent)}', headers = this.get_headers(), cookies = this.cookies)
    
    def username_check(this, username: str) -> response: # NEEDS SESSIONID
        params = this.get_params({
            'unique_id': username
        })
        
        return this.client.get(f'https://www.tiktok.com/api/uniqueid/check/?{this.sign(params, this.userAgent)}', headers = this.get_headers(), cookies = this.cookies)
    
    def account_info(this) -> response:
        return this.client.get(f'https://www.tiktok.com/passport/web/account/info/', headers = this.get_headers(), cookies = this.cookies)
    
    def tiktok_request(this, endpoint, extra_params: dict = {}) -> response:
        params = this.get_params(extra_params)
        
        return this.client.get(f'https://www.tiktok.com/{endpoint}?{this.sign(params, this.userAgent)}', headers = this.get_headers(), cookies = this.cookies)