# How to Block Cloudflare
## with Firewall

This page show you how to block CloudFlare websites with your firewall, preventing from connecting to them.


### With nftables

<details><summary> _click me_ </summary>

```nftables
# make the ip definition
define cf4 = { 103.21.244.0/22, 103.22.200.0/22, 103.31.4.0/22, 104.16.0.0/13, 104.24.0.0/14, 108.162.192.0/18, 131.0.72.0/22, 141.101.64.0/18, 162.158.0.0/15, 172.64.0.0/13, 173.245.48.0/20, 188.114.96.0/20, 190.93.240.0/20, 197.234.240.0/22, 198.41.128.0/17 }
define cf6 = { 2400:cb00::/32, 2405:8100::/32, 2405:b500::/32, 2606:4700::/32, 2803:f800::/32, 2a06:98c0::/29, 2c0f:f248::/32 }

# add the following lines to 
table inet filter {
    chain output {
        ip daddr { $cf4 } counter reject with icmp type admin-prohibited comment "Dropped CF quires"
        ip6 daddr { $cf6 } counter reject with icmpv6 type admin-prohibited comment "Dropped CF quires"
        ...

```

</details>

### With UFW

<details><summary> _click me_ </summary>

```
ufw deny from 103.21.244.0/22
ufw deny from 103.22.200.0/22
ufw deny from 103.31.4.0/22
ufw deny from 104.16.0.0/13
ufw deny from 104.24.0.0/14
ufw deny from 108.162.192.0/18
ufw deny from 131.0.72.0/22
ufw deny from 141.101.64.0/18
ufw deny from 162.158.0.0/15
ufw deny from 172.64.0.0/13
ufw deny from 173.245.48.0/20
ufw deny from 188.114.96.0/20
ufw deny from 190.93.240.0/20
ufw deny from 197.234.240.0/22
ufw deny from 198.41.128.0/17
ufw deny from 2400:cb00::/32
ufw deny from 2405:8100::/32
ufw deny from 2405:b500::/32
ufw deny from 2606:4700::/32
ufw deny from 2803:f800::/32
ufw deny from 2a06:98c0::/29
ufw deny from 2c0f:f248::/32
```

</details>

### With iptables

<details><summary> _click me_ </summary>

```
iptables -A input -s 103.21.244.0/22 -j DROP
iptables -A input -s 103.22.200.0/22 -j DROP
iptables -A input -s 103.31.4.0/22 -j DROP
iptables -A input -s 104.16.0.0/13 -j DROP
iptables -A input -s 104.24.0.0/14 -j DROP
iptables -A input -s 108.162.192.0/18 -j DROP
iptables -A input -s 131.0.72.0/22 -j DROP
iptables -A input -s 141.101.64.0/18 -j DROP
iptables -A input -s 162.158.0.0/15 -j DROP
iptables -A input -s 172.64.0.0/13 -j DROP
iptables -A input -s 173.245.48.0/20 -j DROP
iptables -A input -s 188.114.96.0/20 -j DROP
iptables -A input -s 190.93.240.0/20 -j DROP
iptables -A input -s 197.234.240.0/22 -j DROP
iptables -A input -s 198.41.128.0/17 -j DROP
iptables -A input -s 2400:cb00::/32 -j DROP
iptables -A input -s 2405:8100::/32 -j DROP
iptables -A input -s 2405:b500::/32 -j DROP
iptables -A input -s 2606:4700::/32 -j DROP
iptables -A input -s 2803:f800::/32 -j DROP
iptables -A input -s 2a06:98c0::/29 -j DROP
iptables -A input -s 2c0f:f248::/32 -j DROP
```

</details>

### With Windows Firewall

<details><summary> _click me_ </summary>

```
New-NetFirewallRule -DisplayName "Block CF" -Direction Outbound –LocalPort Any -Action Block -RemoteAddress 103.21.244.0/22
New-NetFirewallRule -DisplayName "Block CF" -Direction Outbound –LocalPort Any -Action Block -RemoteAddress 103.22.200.0/22
New-NetFirewallRule -DisplayName "Block CF" -Direction Outbound –LocalPort Any -Action Block -RemoteAddress 103.31.4.0/22
New-NetFirewallRule -DisplayName "Block CF" -Direction Outbound –LocalPort Any -Action Block -RemoteAddress 104.16.0.0/13
New-NetFirewallRule -DisplayName "Block CF" -Direction Outbound –LocalPort Any -Action Block -RemoteAddress 104.24.0.0/14
New-NetFirewallRule -DisplayName "Block CF" -Direction Outbound –LocalPort Any -Action Block -RemoteAddress 108.162.192.0/18
New-NetFirewallRule -DisplayName "Block CF" -Direction Outbound –LocalPort Any -Action Block -RemoteAddress 131.0.72.0/22
New-NetFirewallRule -DisplayName "Block CF" -Direction Outbound –LocalPort Any -Action Block -RemoteAddress 141.101.64.0/18
New-NetFirewallRule -DisplayName "Block CF" -Direction Outbound –LocalPort Any -Action Block -RemoteAddress 162.158.0.0/15
New-NetFirewallRule -DisplayName "Block CF" -Direction Outbound –LocalPort Any -Action Block -RemoteAddress 172.64.0.0/13
New-NetFirewallRule -DisplayName "Block CF" -Direction Outbound –LocalPort Any -Action Block -RemoteAddress 173.245.48.0/20
New-NetFirewallRule -DisplayName "Block CF" -Direction Outbound –LocalPort Any -Action Block -RemoteAddress 188.114.96.0/20
New-NetFirewallRule -DisplayName "Block CF" -Direction Outbound –LocalPort Any -Action Block -RemoteAddress 190.93.240.0/20
New-NetFirewallRule -DisplayName "Block CF" -Direction Outbound –LocalPort Any -Action Block -RemoteAddress 197.234.240.0/22
New-NetFirewallRule -DisplayName "Block CF" -Direction Outbound –LocalPort Any -Action Block -RemoteAddress 198.41.128.0/17
New-NetFirewallRule -DisplayName "Block CF" -Direction Outbound –LocalPort Any -Action Block -RemoteAddress 2400:cb00::/32
New-NetFirewallRule -DisplayName "Block CF" -Direction Outbound –LocalPort Any -Action Block -RemoteAddress 2405:8100::/32
New-NetFirewallRule -DisplayName "Block CF" -Direction Outbound –LocalPort Any -Action Block -RemoteAddress 2405:b500::/32
New-NetFirewallRule -DisplayName "Block CF" -Direction Outbound –LocalPort Any -Action Block -RemoteAddress 2606:4700::/32
New-NetFirewallRule -DisplayName "Block CF" -Direction Outbound –LocalPort Any -Action Block -RemoteAddress 2803:f800::/32
New-NetFirewallRule -DisplayName "Block CF" -Direction Outbound –LocalPort Any -Action Block -RemoteAddress 2a06:98c0::/29
New-NetFirewallRule -DisplayName "Block CF" -Direction Outbound –LocalPort Any -Action Block -RemoteAddress 2c0f:f248::/32
```

</details>

### With COMODO Firewall

<details><summary> _click me_ </summary>

1. Export your configuration to file.
2. Open the file and search for `<BlockedAddresses>`
3. Copy & paste below text to between `<BlockedAddresses>` and `</BlockedAddresses>`.
4. Save the file and import it with new profile name.
5. Apply the profile.

```
<ArrayItem Type="4" Name=""><Address Type="1"><IPV4 AddrType="2" AddrStart="103.21.244.0" AddrEnd="103.21.247.255" /></Address></ArrayItem>
<ArrayItem Type="4" Name=""><Address Type="1"><IPV4 AddrType="2" AddrStart="103.22.200.0" AddrEnd="103.22.203.255" /></Address></ArrayItem>
<ArrayItem Type="4" Name=""><Address Type="1"><IPV4 AddrType="2" AddrStart="103.31.4.0" AddrEnd="103.31.7.255" /></Address></ArrayItem>
<ArrayItem Type="4" Name=""><Address Type="1"><IPV4 AddrType="2" AddrStart="104.16.0.0" AddrEnd="104.23.255.255" /></Address></ArrayItem>
<ArrayItem Type="4" Name=""><Address Type="1"><IPV4 AddrType="2" AddrStart="104.24.0.0" AddrEnd="104.27.255.255" /></Address></ArrayItem>
<ArrayItem Type="4" Name=""><Address Type="1"><IPV4 AddrType="2" AddrStart="108.162.192.0" AddrEnd="108.162.255.255" /></Address></ArrayItem>
<ArrayItem Type="4" Name=""><Address Type="1"><IPV4 AddrType="2" AddrStart="131.0.72.0" AddrEnd="131.0.75.255" /></Address></ArrayItem>
<ArrayItem Type="4" Name=""><Address Type="1"><IPV4 AddrType="2" AddrStart="141.101.64.0" AddrEnd="141.101.127.255" /></Address></ArrayItem>
<ArrayItem Type="4" Name=""><Address Type="1"><IPV4 AddrType="2" AddrStart="162.158.0.0" AddrEnd="162.159.255.255" /></Address></ArrayItem>
<ArrayItem Type="4" Name=""><Address Type="1"><IPV4 AddrType="2" AddrStart="172.64.0.0" AddrEnd="172.71.255.255" /></Address></ArrayItem>
<ArrayItem Type="4" Name=""><Address Type="1"><IPV4 AddrType="2" AddrStart="173.245.48.0" AddrEnd="173.245.63.255" /></Address></ArrayItem>
<ArrayItem Type="4" Name=""><Address Type="1"><IPV4 AddrType="2" AddrStart="188.114.96.0" AddrEnd="188.114.111.255" /></Address></ArrayItem>
<ArrayItem Type="4" Name=""><Address Type="1"><IPV4 AddrType="2" AddrStart="190.93.240.0" AddrEnd="190.93.255.255" /></Address></ArrayItem>
<ArrayItem Type="4" Name=""><Address Type="1"><IPV4 AddrType="2" AddrStart="197.234.240.0" AddrEnd="197.234.243.255" /></Address></ArrayItem>
<ArrayItem Type="4" Name=""><Address Type="1"><IPV4 AddrType="2" AddrStart="198.41.128.0" AddrEnd="198.41.255.255" /></Address></ArrayItem>
```

</details>

### With PeerBlock

<details><summary> _click me_ </summary>

```
CloudFlare:103.21.244.0-103.21.247.255
CloudFlare:103.22.200.0-103.22.203.255
CloudFlare:103.31.4.0-103.31.7.255
CloudFlare:104.16.0.0-104.23.255.255
CloudFlare:104.24.0.0-104.27.255.255
CloudFlare:108.162.192.0-108.162.255.255
CloudFlare:131.0.72.0-131.0.75.255
CloudFlare:141.101.64.0-141.101.127.255
CloudFlare:162.158.0.0-162.159.255.255
CloudFlare:172.64.0.0-172.71.255.255
CloudFlare:173.245.48.0-173.245.63.255
CloudFlare:188.114.96.0-188.114.111.255
CloudFlare:190.93.240.0-190.93.255.255
CloudFlare:197.234.240.0-197.234.243.255
CloudFlare:198.41.128.0-198.41.255.255
```

</details>
