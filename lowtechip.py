'''
lowtechip
~~~~~~~~~

> python3 lowtechip.py <path/to/conf.json>

Rename conf.example.json to something else and adjust it to your needs.
You most likely want to change only notify_url and daemon_interval first.
Then run `python3 lowtechip.py yourconf.json`
'''

import datetime
import json
import pathlib
import sys
import time
import urllib.parse

import requests




class Lowtechip:
    conf: dict
    prev_ip: str = 'empty'


    def __init__(self) -> None:
        if len(sys.argv) < 2:
            # print("print usage here later")
            print(__doc__)
            sys.exit(0)

        conf_file: pathlib.Path = pathlib.Path(sys.argv[1]).resolve()

        if not conf_file.is_file():
            print(f"conf_file does not exist or is not a file: {conf_file}")
            sys.exit(1)

        self.conf: dict = json.loads(s=conf_file.read_text())

        print(f"loaded conf = {json.dumps(obj=self.conf, ensure_ascii=False, indent=4)}")


    def daemon(self):
        is_first_iter: bool = True

        while True:
            try:
                if not is_first_iter:
                    self.screen_msg(f"next check on {datetime.datetime.fromtimestamp(time.time() + self.conf['daemon_interval']).strftime('%Y-%m-%d %H:%M:%S')}")
                    time.sleep(self.conf['daemon_interval'])
                else:
                    is_first_iter = False

                self.screen_msg("fetching external ip")
                ip: str = self.fetch_ip()

                if ip == self.prev_ip:
                    self.screen_msg(f"  no change: {ip}")
                    continue

                self.screen_msg(f"  change detected: {self.prev_ip} -> {ip}")

                self.screen_msg(f"notifying {urllib.parse.urlparse(url=self.conf['notify_url']).netloc}")

                self.send_ip(ip=ip)
                self.screen_msg("  ok")

                self.prev_ip = ip

            except KeyboardInterrupt:
                self.screen_msg("\nexiting...")
                sys.exit(0)

            except Exception as e:
                self.screen_msg(f"  BOO: {e}")
                self.screen_msg("  trying again soon")


    def fetch_ip(self) -> str:
        r: requests.Response = requests.get(url=self.conf['ip_api_endpoint'], timeout=self.conf['req_timeout'], headers=self.conf['req_headers'])
        r.raise_for_status()

        ip: str = r.text.strip()

        if not ip:
            raise Exception('Got no data in response.')

        return ip


    def send_ip(self, ip: str) -> requests.Response:
        r: requests.Response = requests.post(url=self.conf['notify_url'], data={'ip': ip}, timeout=self.conf['req_timeout'], headers=self.conf['req_headers'])
        r.raise_for_status()
        return r


    @staticmethod
    def screen_msg(msg: str, /) -> None:
        print(f"{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')} | {msg}")




if __name__ == '__main__':
    Lowtechip().daemon()
