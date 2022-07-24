import os
 
try:
    import httpx, asyncio, tasksio, random, threading, pystyle, cursor, time, sys
except:
    z = "python -m pip install "
    os.system("%shttpx" % (z))
    os.system("%sasyncio" % (z))
    os.system("%stasksio" % (z))
    os.system("%spystyle" % (z))
    os.system("%scursor" % (z))


class TikTok:
    def __init__(self):
        cursor.hide()
        os.system('cls' if os.name == 'nt' else 'clear')
        self.username = pystyle.Write.Input(
            "\n [ ? ] Username > ", pystyle.Colors.blue_to_red, interval=0.0025
        )

        self.report_count = 0
        self.requests = 0

        self.report_type = pystyle.Write.Input(
            "\n Report Types:\n   317 - Underage \n   9010 - Spam Posts \n   90031 - Promotion of criminal activities\n\n [ ? ] Report Type > ",
            pystyle.Colors.blue_to_red,
            interval=0.0025,
        )
        if str(self.report_type) not in ("317", "9010", "90031"):
            return print(
                pystyle.Colorate.Horizontal(
                    pystyle.Colors.blue_to_red, f" [ ! ] Invalid Report Type.", 1
                )
            )
        else:
            self.report_reason = str(self.report_type)
            print(
                pystyle.Colorate.Horizontal(
                    pystyle.Colors.blue_to_red, f"\n [ * ] Sending Reports...\n", 1
                )
            )

        self.user_id = ""
        self.secuid = ""

        self.lock = threading.Lock()
        self.getinfo()

    def print(self, arg):
        self.lock.acquire()
        print(arg)
        self.lock.release()

    def title(self):
        _t_ = time.time()
        while True:
            os.system(
                f"title TikTok Reporter ^| Reports: {self.report_count} ^| Reqs: {self.requests} ^| Elapsed: {round(time.time()- _t_, 1)}s"
            ) if "nt" in os.name else sys.stdout.write(
                f"\x1b]2;TikTok Reporter | Reports: {self.report_count} | Reqs: {self.requests} | Elapsed: {round(time.time()- _t_, 1)}s\x07"
            )
            time.sleep(0.1)

    def getinfo(self):
        with httpx.Client() as client:
            client.headers = {
                "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:99.0) Gecko/20100101 Firefox/99.0",
                "Cookie": "msToken=zgbEqIjfSC7M7QdTTpHDkpWLtnY4JnK22HiSE1iHCRGBBYY_36Gm-gMDqyGLBjpPE2svzjVPNGWyMFYUUEBwmGkr5y2qQuKmfjfTh0i2hfOsb_B7jfDrbd9a4IhjMLPyUIRNIZLqzG6PldNNXA==",
            }
            DATA = client.get(
                "https://www.tiktok.com/api/user/detail/?device_id=7098862702289995269&uniqueId=%s"
                % (self.username)
            ).json()["userInfo"]["user"]

            self.user_id = DATA["id"]
            self.username = DATA["uniqueId"]
            self.secuid = DATA["secUid"]

        asyncio.get_event_loop().run_until_complete(self.start())

    async def start(self):
        threading.Thread(target=self.title).start()
        while True:
            async with tasksio.TaskPool(workers=1_000) as pool:
                for x in range(1_000):
                    await pool.put(self.report())

    async def report(self):
        while True:
            try:
                async with httpx.AsyncClient() as client:
                    client.headers[
                        "user-agent"
                    ] = "Mozilla/5.0 (Linux; U; Android 4.4.2; en-us; SCH-I535 Build/KOT49H) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30"
                    req = await client.get(
                        f'https://www.tiktok.com/aweme/v1/aweme/feedback/?aid=1988&app_language=TK&channel={random.choice(["tiktok_web", "googleplay", "App%20Store"])}&current_region=TK&device_id={random.randint(1000000000000000000, 9999999999999999999)}&lang=en&nickname={self.username}&object_id=76493735542&os=1337&owner_id={self.user_id}&reason={self.report_reason}&region=TK&report_type=user&secUid={self.secuid}&target={self.user_id}&tz_name=nigger'
                    )
                    self.requests += 1
                    if "Thanks for your feedback" in req.text:
                        self.report_count += 1
                        self.print(
                            pystyle.Colorate.Horizontal(
                                pystyle.Colors.blue_to_red,
                                f" [ + ] Sent Report. ({self.report_count})",
                                1,
                            )
                        )
                    else:
                        await self.report()
            except:
                await self.report()


if __name__ == "__main__":
    TikTok()
