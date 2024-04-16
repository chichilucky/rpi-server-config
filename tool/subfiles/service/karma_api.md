## Karma API

- Operated by `Crimeflare #Karma` with `No log` policy.
  - There is a rate-limit and anti-attack system so please be nice.
- List data is almost identical to [this git data](http://crimeflare.eu.org).

There are many wide-range APIs live on Karma.

In this page we explain 2 read-only APIs.


Replace the (base url) to:
| Type | URL |
| -- | -- |
| Clearnet | `https://karma.crimeflare.eu.org:1984/api/` |
| Tor | `http://karma.im5wixghmfmt7gf7wb4xrgdm6byx2gj26zn47da6nwo7xvybgxnqryid.onion/api/` |

-----

> Cloudflare Domains Lookup

- For looking up domain's existence as a [MITM domain](../../cloudflare_users/domains/README.md).
- Also try: `Listed as Cloudflare` website
  - [Clearnet](https://karma.crimeflare.eu.org:1984/api/is/cloudflare/html/)
  - [Tor](http://karma.im5wixghmfmt7gf7wb4xrgdm6byx2gj26zn47da6nwo7xvybgxnqryid.onion/api/is/cloudflare/html/)

| ? | ? |
| -- | -- |
| Location | `(base url)is/cloudflare/` |
| Request Method | `POST` |
| Input | **Single Question**<br>`f` or `u` is required. `ignore_cfowned` is optional.<br>`f` FQDN (e.g. `www.google.com`)<br>`u` URL (e.g. `https://www.google.com/`)<br>`ignore_cfowned` Existence (If set, return FALSE when the domain is owned by CloudFlare Inc.)<br><br>**Multiple Questions** (max 200 domains)<br>`ff` is required. `ignore_cfowned` is optional.<br>`ff` List of FQDN separated by `,` (e.g. `www.google.com,blog.emsisoft.com,youtu.be`)<br>`ignore_cfowned` Existence (If set, return FALSE when the domain is owned by CloudFlare Inc.) |
| Output | JSON value as array.<br>**Single Question**<br>If 2nd value(j[1]) is true then the input is Cloudflare.<br>`[false,false]` (Error or not Cloudflare)<br>`[true,false]` (Not Cloudflare)<br>`[true,true]` (Cloudflare)<br><br>**Multiple Questions**<br>Array pair of `question:true\|false`.<br>`{'example.com':false,...}` (Not Cloudflare)<br>`{'example.com':true,...}` (Cloudflare) |
| cURL Example | `curl -X POST -F 'f=www.example.com' -k --http2 https://clearnet/api/is/cloudflare/`<br>`curl -x socks5h://127.0.0.1:9050 -X POST -F 'f=www.example.com' http://onion/api/is/cloudflare/`<br>`curl -X POST -F 'ff=www.emsisoft.com,joinmastodon.org,framagit.org' -k --http2 https://clearnet/api/is/cloudflare/` |


> Anti-Tor Lookup

For looking up website's existence in the [known Anti-tor list](../../anti-tor_users/domains/README.md).

| ? | ? |
| -- | -- |
| Location | `(base url)is/antitor/` |
| Request Method | `POST` |
| Input | `f` is required.<br>`f` FQDN (e.g. `www.google.com`) |
| Output | JSON value as array. If 2nd value(j[1]) is true then the input is AntiTor.<br>`[false,false]` (Error or not AntiTor)<br>`[true,false]` (Not AntiTor)<br>`[true,true]` (AntiTor) |
| cURL Example | `curl -X POST -F 'f=www.example.com' -k --http2 https://clearnet/api/is/antitor/`<br>`curl -x socks5h://127.0.0.1:9050 -X POST -F 'f=www.example.com' http://onion/api/is/antitor/` |
