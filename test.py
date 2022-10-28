import requests

url = "https://api16-va.tiktokv.com/aweme/v1/aweme/feedback/"

querystring = {
    "report_type": "video",
    "object_id": 7152985345364184326, #"7158973812602572078",
    "owner_id": 7079788502129869829, #"7141531689000551470",
    "isFirst": "1",
    "report_desc": "",
    "uri": "",
    "reason": "9005",
    "category": "",
    # "request_tag_from": "h5",
    # "os_api": "25",
    # "device_type": "SM-G988N",
    # "ssmix": "a",
    # "manifest_version_code": "160904",
    # "dpi": "320",
    # "carrier_region": "IE",
    # "uoo": "0",
    # "region": "FR",
    # "carrier_region_v2": "208",
    # "app_name": "musically_go",
    # "version_name": "16.9.4",
    # "timezone_offset": "7200",
    # "ts": "1666892833",
    # "ab_version": "16.9.4",
    # "pass-route": "1",
    # "cpu_support64": "true",
    # "pass-region": "1",
    # "storage_type": "0",
    # "ac2": "wifi",
    # "ac": "wifi",
    # "app_type": "normal",
    # "host_abi": "armeabi-v7a",
    # "channel": "googleplay",
    # "update_version_code": "160904",
    # "_rticket": "1666892834689",
    # "device_platform": "android",
    # "iid": "7159249365869414149",
    # "build_number": "16.9.4",
    # "locale": "fr",
    # "op_region": "IE",
    # "version_code": "160904",
    # "timezone_name": "Africa/Harare",
    # "cdid": "7269b691-32ec-454e-b6c7-b96198955ea0",
    # "openudid": "46308452a65fb9cd",
    # "sys_region": "FR",
    # "device_id": "6712029815367206401",
    # "app_language": "fr",
    # "resolution": "900*1600",
    # "device_brand": "samsung",
    # "language": "fr",
    # "os_version": "7.1.2",
    # "aid": "1340"
}

headers = {
    "accept-encoding": "gzip",
    "passport-sdk-version": "17",
    "sdk-version": "2",
    "x-ss-req-ticket": "1666892834690",
    "cookie": "store-idc=alisg; store-country-code=kr; store-country-code-src=did; install_id=7159249365869414149; ttreq=1$5934e89fb35a03b18ec980ed435e1e4b3c192824; odin_tt=504da9f656f582abc312bc8457c091ebaf3536c30ba13261e0021d42fae298fd1ed5de1ff248517fa8abecf8092c67b069b0343e01a2b254c94b67d5728d3477cf58402a4354902a72e4d3d5a11de215; msToken=BdGidevHXarA0Kymau7ta9mtw5y_Gp9mh50qjpfL3tb_r_7SSiQ-h_0paMNBE8YnvKkQyKA1sMBdJ8qnyN3o8JbcT-9aDQd2-aurIwvmJw4a8dUyD1vEJ_A=",
    "x-gorgon": "040480c6400028766ec53fdf5c792abf37fdee6b40c593715c24",
    "x-khronos": "1666892834",
    "host": "api16-va.tiktokv.com",
    "connection": "Keep-Alive",
    "user-agent": "okhttp/3.10.0.1"
}

response = requests.get(url, headers=headers, params=querystring)

print(response.text)