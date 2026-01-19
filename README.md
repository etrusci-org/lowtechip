# lowtechip

A lowtech solution to monitor changes in the current machine's public IP and notify a remote server when such changes occur.




## Requirements

- Linux, Windows or Mac operating system.
- [Python](https://www.python.org) `>= 3.11.2`
  - [requests](https://github.com/psf/requests) `>= 2.32.5`




## Setup

1. Install the requirements.
2. Copy and rename **[conf.example.json](./conf.example.json)** to **myconf.json**, then adjust the values in **myconf.json** to your needs. You most likely want to change only `notify_url` and `daemon_interval` first.




## Usage

Once done with the setup, you can run **lowtechip** like so:

```cli
python3 lowtechip.py <path/to/yourconf.json>
```

E.g.:

```cli
python3 lowtechip.py myconf.json
```




## Thanks to

- **[ipify.org](https://ipify.org)** for the nifty public IP address API which **lowtechip** uses as default endpoint.
