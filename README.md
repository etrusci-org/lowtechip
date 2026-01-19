# lowtechip

A lowtech solution to monitor changes in the current machine's public IP and notify a remote server when such changes occur.




## Requirements

- Linux, Windows or Mac operating system.
- [Python](https://www.python.org) `>= 3.11.2`
  - [requests](https://github.com/psf/requests) `>= 2.32.5`




## Setup

1. Install the requirements.
2. Copy **[remote.example.php](./remote.example.php)** to your webserver. Or use the example code as a starting point for your own script in a language of your choice.
3. Copy and rename **[conf.example.json](./conf.example.json)** to **myconf.json**, then adjust the values in **myconf.json** to your needs. You most likely want to change only `notify_url` and `daemon_interval` first.




## Usage

Once done with the setup, you can run **lowtechip** like so:

```cli
python3 lowtechip.py path/to/myconf.json
```

Stop it with `CTRL+C` or close the terminal.




**Example output**:

```txt
       /~~~~~~~~~~~~~~~~~\
        l o w t e c h i p
       \~~~~~~~~~~~~~~~~~/

     notify_url = http://localhost/lowtechip/remote.example.php
daemon_interval = 10.0
ip_api_endpoint = https://api64.ipify.org
    req_timeout = 10.0
    req_headers = {'user-agent': 'lowtechip'}

Press [Enter] to start.

2026-01-19 18:31:51 | fetching puplic ip
2026-01-19 18:31:52 |   change detected: empty -> 130.195.221.167
2026-01-19 18:31:52 | notifying localhost
2026-01-19 18:31:52 |   ok
2026-01-19 18:32:02 | fetching puplic ip
2026-01-19 18:32:03 |   no change: 130.195.221.167
2026-01-19 18:32:13 | fetching puplic ip
2026-01-19 18:32:14 |   change detected: 130.195.221.167 -> 146.70.170.21
2026-01-19 18:32:14 | notifying localhost
2026-01-19 18:32:14 |   ok
2026-01-19 18:32:24 | fetching puplic ip
2026-01-19 18:32:24 |   no change: 146.70.170.21
2026-01-19 18:32:34 | fetching puplic ip
2026-01-19 18:32:35 |   change detected: 146.70.170.21 -> 159.26.116.11
2026-01-19 18:32:35 | notifying localhost
2026-01-19 18:32:35 |   BOO: 400 Client Error: Bad Request for url: http://localhost/lowtechip/remote.example.php
2026-01-19 18:32:35 |   will try again
2026-01-19 18:32:45 | fetching puplic ip
2026-01-19 18:32:46 |   change detected: 146.70.170.21 -> 159.26.116.11
2026-01-19 18:32:46 | notifying localhost
2026-01-19 18:32:46 |   BOO: 400 Client Error: Bad Request for url: http://localhost/lowtechip/remote.example.php
2026-01-19 18:32:46 |   will try again
2026-01-19 18:32:56 | fetching puplic ip
2026-01-19 18:32:57 |   change detected: 146.70.170.21 -> 159.26.116.11
2026-01-19 18:32:57 | notifying localhost
2026-01-19 18:32:57 |   ok
2026-01-19 18:33:07 | fetching puplic ip
2026-01-19 18:33:07 |   change detected: 159.26.116.11 -> 194.126.177.49
2026-01-19 18:33:07 | notifying localhost
2026-01-19 18:33:07 |   ok
2026-01-19 18:33:17 | fetching puplic ip
2026-01-19 18:33:18 |   no change: 194.126.177.49
2026-01-19 18:33:28 | fetching puplic ip
2026-01-19 18:33:28 |   no change: 194.126.177.49
^C
exiting...
```



## Thanks to

- **[ipify.org](https://ipify.org)** for the nifty public IP address API which **lowtechip** uses as default endpoint.




## License

**lowtechip** is licensed under **[The Unlicense](./LICENSE.md)**.
