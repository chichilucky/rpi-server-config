# How to Block Cloudflare
## with Proxy

This page show you how to block CloudFlare websites with proxy.


### With PAC Script

<details><summary> _click me_ </summary>

- Save below to `pac.txt` and load it with PAC-supported browser (e.g. `file:///root/pac.txt`)

```
function FindProxyForURL(url, host){

var hip = dnsResolve(host);
if (
isInNet(hip,"103.21.244.1","255.255.252.0")
||isInNet(hip,"103.22.200.1","255.255.252.0")
||isInNet(hip,"103.31.4.1","255.255.252.0")
||isInNet(hip,"104.16.0.1","255.248.0.0")
||isInNet(hip,"104.24.0.1","255.252.0.0")
||isInNet(hip,"108.162.192.1","255.255.192.0")
||isInNet(hip,"131.0.72.1","255.255.252.0")
||isInNet(hip,"141.101.64.1","255.255.192.0")
||isInNet(hip,"162.158.0.1","255.254.0.0")
||isInNet(hip,"172.64.0.1","255.248.0.0")
||isInNet(hip,"173.245.48.1","255.255.240.0")
||isInNet(hip,"188.114.96.1","255.255.240.0")
||isInNet(hip,"190.93.240.1","255.255.240.0")
||isInNet(hip,"197.234.240.1","255.255.252.0")
||isInNet(hip,"198.41.128.1","255.255.128.0")
){return "SOCKS5 0.0.0.0:7";}

return "DIRECT";

}
```

</details>

### With ShadowSocks ACL

<details><summary> _click me_ </summary>

```
[outbound_block_list]
103.21.244.0/22
103.22.200.0/22
103.31.4.0/22
104.16.0.0/13
104.24.0.0/14
108.162.192.0/18
131.0.72.0/22
141.101.64.0/18
162.158.0.0/15
172.64.0.0/13
173.245.48.0/20
188.114.96.0/20
190.93.240.0/20
197.234.240.0/22
198.41.128.0/17
2400:cb00::/32
2405:8100::/32
2405:b500::/32
2606:4700::/32
2803:f800::/32
2a06:98c0::/29
2c0f:f248::/32
```

</details>

### With Privoxy ACL

<details><summary> _click me_ </summary>

```
deny-access 127.0.0.1 103.21.244.0/22
deny-access 127.0.0.1 103.22.200.0/22
deny-access 127.0.0.1 103.31.4.0/22
deny-access 127.0.0.1 104.16.0.0/13
deny-access 127.0.0.1 104.24.0.0/14
deny-access 127.0.0.1 108.162.192.0/18
deny-access 127.0.0.1 131.0.72.0/22
deny-access 127.0.0.1 141.101.64.0/18
deny-access 127.0.0.1 162.158.0.0/15
deny-access 127.0.0.1 172.64.0.0/13
deny-access 127.0.0.1 173.245.48.0/20
deny-access 127.0.0.1 188.114.96.0/20
deny-access 127.0.0.1 190.93.240.0/20
deny-access 127.0.0.1 197.234.240.0/22
deny-access 127.0.0.1 198.41.128.0/17
deny-access 127.0.0.1 2400:cb00::/32
deny-access 127.0.0.1 2405:8100::/32
deny-access 127.0.0.1 2405:b500::/32
deny-access 127.0.0.1 2606:4700::/32
deny-access 127.0.0.1 2803:f800::/32
deny-access 127.0.0.1 2a06:98c0::/29
deny-access 127.0.0.1 2c0f:f248::/32
```

</details>

### With Dante Socks

<details><summary> _click me_ </summary>

```
socks pass {
   from: 0.0.0.0/0 to: 103.21.244.0/22
   command: connect
   redirect to: 0.0.0.0 port = 7
}
socks pass {
   from: 0.0.0.0/0 to: 103.22.200.0/22
   command: connect
   redirect to: 0.0.0.0 port = 7
}
socks pass {
   from: 0.0.0.0/0 to: 103.31.4.0/22
   command: connect
   redirect to: 0.0.0.0 port = 7
}
socks pass {
   from: 0.0.0.0/0 to: 104.16.0.0/13
   command: connect
   redirect to: 0.0.0.0 port = 7
}
socks pass {
   from: 0.0.0.0/0 to: 104.24.0.0/14
   command: connect
   redirect to: 0.0.0.0 port = 7
}
socks pass {
   from: 0.0.0.0/0 to: 108.162.192.0/18
   command: connect
   redirect to: 0.0.0.0 port = 7
}
socks pass {
   from: 0.0.0.0/0 to: 131.0.72.0/22
   command: connect
   redirect to: 0.0.0.0 port = 7
}
socks pass {
   from: 0.0.0.0/0 to: 141.101.64.0/18
   command: connect
   redirect to: 0.0.0.0 port = 7
}
socks pass {
   from: 0.0.0.0/0 to: 162.158.0.0/15
   command: connect
   redirect to: 0.0.0.0 port = 7
}
socks pass {
   from: 0.0.0.0/0 to: 172.64.0.0/13
   command: connect
   redirect to: 0.0.0.0 port = 7
}
socks pass {
   from: 0.0.0.0/0 to: 173.245.48.0/20
   command: connect
   redirect to: 0.0.0.0 port = 7
}
socks pass {
   from: 0.0.0.0/0 to: 188.114.96.0/20
   command: connect
   redirect to: 0.0.0.0 port = 7
}
socks pass {
   from: 0.0.0.0/0 to: 190.93.240.0/20
   command: connect
   redirect to: 0.0.0.0 port = 7
}
socks pass {
   from: 0.0.0.0/0 to: 197.234.240.0/22
   command: connect
   redirect to: 0.0.0.0 port = 7
}
socks pass {
   from: 0.0.0.0/0 to: 198.41.128.0/17
   command: connect
   redirect to: 0.0.0.0 port = 7
}
socks pass {
   from: 0.0.0.0/0 to: 2400:cb00::/32
   command: connect
   redirect to: 0.0.0.0 port = 7
}
socks pass {
   from: 0.0.0.0/0 to: 2405:8100::/32
   command: connect
   redirect to: 0.0.0.0 port = 7
}
socks pass {
   from: 0.0.0.0/0 to: 2405:b500::/32
   command: connect
   redirect to: 0.0.0.0 port = 7
}
socks pass {
   from: 0.0.0.0/0 to: 2606:4700::/32
   command: connect
   redirect to: 0.0.0.0 port = 7
}
socks pass {
   from: 0.0.0.0/0 to: 2803:f800::/32
   command: connect
   redirect to: 0.0.0.0 port = 7
}
socks pass {
   from: 0.0.0.0/0 to: 2a06:98c0::/29
   command: connect
   redirect to: 0.0.0.0 port = 7
}
socks pass {
   from: 0.0.0.0/0 to: 2c0f:f248::/32
   command: connect
   redirect to: 0.0.0.0 port = 7
}
```

</details>

