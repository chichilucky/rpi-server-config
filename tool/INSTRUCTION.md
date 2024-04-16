# List Instructions

![](image/imnotarobot.gif)

---

<details>
<summary><h3>Website is using Cloudflare</h3></summary>

- **Cloudflare users** | [**List Directory**](cloudflare_users/)

| List name | Description |
| --- | --- |
| [/domains/*/cloudflare_?.txt](cloudflare_users/domains) | Split files (base domain)     |
| [ex_cloudflare_users.md](cloudflare_users/ex_cloudflare_users.md)     | Domains which used Cloudflare in the past, not anymore     |
| [cloudflare_supporter.md](cloudflare_users/cloudflare_supporter.md) | who is supporting, endorsing, loving, or defending Cloudflare |


- **Cloudflare Corporation** | [**List Directory**](cloudflare_inc/)

| List name | Description |
| --- | --- |
| [cloudflare_CIDR_v4.txt](cloudflare_inc/cloudflare_CIDR_v4.txt)     | IPv4 CIDR owned by Cloudflare     |
| [cloudflare_CIDR_v6.txt](cloudflare_inc/cloudflare_CIDR_v6.txt)     | IPv6 CIDR owned by Cloudflare     |
| [cloudflare_range_v4.txt](cloudflare_inc/cloudflare_range_v4.txt) | IPv4 range owned by Cloudflare |
| [cloudflare_owned_ASN.txt](cloudflare_inc/cloudflare_owned_ASN.txt)     | AS network owned by Cloudflare    |
| [cloudflare_owned_NS.txt](cloudflare_inc/cloudflare_owned_NS.txt)     | Name Server owned by Cloudflare    |
| [cloudflare_owned_domains.txt](cloudflare_inc/cloudflare_owned_domains.txt)     | Domains owned by Cloudflare     |
| [cloudflare_owned_onions.txt](cloudflare_inc/cloudflare_owned_onions.txt)     | Tor .onions owned by Cloudflare     |
| [cloudflare_members.md](cloudflare_inc/cloudflare_members.md) | Cloudflare employer, employee, ex-employee |

**How to detect Cloudflare?**

There are many ways to detect it:

- Add-on "[Block Cloudflare MITM Attack!](subfiles/addon/bcma.md)" will help your Cloudflare collection.
- Add-on "[Are links vulnerable to MITM attack?](subfiles/addon/ismm.md)" will tell you which link is Cloudflared.
- Visit a website via Tor or VPN, and you will be greeted by "_Attention Required! Cloudflare_" or "_Checking your browser_" webpage.
- Karma's ["Find Cloudflare Domains" API](subfiles/service/karma_api.md)
- Use "[Search domain](subfiles/service/ombrelo.md)" webpage.
- Search [cloudflare domain list](cloudflare_users/domains/).
  - [CfDomains report tool](tool/cfdomains/README.md)
- Dig "[NS record](https://www.digwebinterface.com/?hostnames=emsisoft.com&type=NS&ns=resolver&useresolver=8.8.4.4&nameservers=)" of the domain.

```
emsisoft.com.		21599	IN	NS	bella.ns.cloudflare.com.
emsisoft.com.		21599	IN	NS	dom.ns.cloudflare.com.
```

Cloudflare [Custom Name Server](https://web.archive.org/web/20210511180344/https://support.cloudflare.com/hc/en-us/articles/200169006-Setting-up-Custom-Nameservers-at-Cloudflare)
```
bitcoinmagazine.com.	21599	IN	NS	btc.ns.bitcoinmagazine.com.
bitcoinmagazine.com.	21599	IN	NS	xbt.ns.bitcoinmagazine.com.

btc.ns.bitcoinmagazine.com. 899	IN	A	162.159.8.190 --> 162.159.8.0/24 (CF)
xbt.ns.bitcoinmagazine.com. 899	IN	A	162.159.9.117 --> 162.159.9.0/24 (CF)
```

- Dig "[A record](https://www.digwebinterface.com/?hostnames=dev.qubes-os.org&type=A&ns=resolver&useresolver=8.8.4.4&nameservers=)" of the FQDN, then [check the IP's owner](https://ipinfo.io/104.18.228.122).

```
dev.qubes-os.org.	299	IN	A	104.18.228.122

ASN AS13335 Cloudflare, Inc.
Organization Cloudflare, Inc.
Route 104.18.224.0/20
```

```
IMPORTANT: Please add only "Base Domain"

    if "community.example.com" is using Cloudflare
        add "example.com"

    if "www.example.co.uk" is using Cloudflare
        add "example.co.uk"

    if "example.net" is using Cloudflare
        add "example.net"

... to cloudflare_e.txt
```

**But the website X no longer using Cloudflare!**

Are you sure? *Remove* it from /split/ list and *add* to "[ex_cloudflare_users.md](cloudflare_users/ex_cloudflare_users.md)".

</details>

------

<details>
<summary><h3>Website is NOT using Cloudflare</h3></summary>

- **Non-Cloudflare CDN users** | [**List Directory**](not_cloudflare/)

| List name | Description |
| -------- | -------- |
| [/ASN/?.txt](not_cloudflare/ASN/)     |  ASN    |
| [/CIDR/?.txt](not_cloudflare/CIDR/)     |  CIDR    |
| [/NS/?.txt](not_cloudflare/NS/)     |  NS    |

```
CDN_Code

Z1 Amazon
Z2 Akamai
//Z3 Cloudflare
Z4 Imperva
Z5 Google
Z6 Microsoft
Z7 INAP & SingleHop
Z8 Sucuri
Z9 Fastly
```

- Add-on "[Which website rejected me?](subfiles/addon/urjm.md)" will help your domain collection.

![](image/siteground.jpg)

- Above is how Siteground-hosted ([INAP](https://www.inap.com/press-release/inap-completes-acquisition-singlehop/);[Singlehop](https://www.siteground.com/blog/siteground-partners-singlehop/)) sites often appear to Tor visitors when timeouts/tarpitting doesn't occur.

Some websites combine other companies (e.g. Amazon AWS, Google Cloud, DDoS-GUARD) _with_ the Cloudflare business model.

![](image/cloudflare_with_ddosguard.jpg)

</details>

------

<details>
<summary><h3>Website is rejecting Tor visitor</h3></summary>

- **Anti-Tor users** | [**List Directory**](anti-tor_users/)

| List name | Description |
| -------- | -------- |
| [/domains/*/antitor_?.txt](anti-tor_users/domains/)     | Split files (FQDN) |
| [/misc/hostility.md](anti-tor_users/misc/hostility.md) | **Does NOT block Tor access BUT** Domain and Comment |

- Add-on "[Which website rejected me?](subfiles/addon/urjm.md)" will help your domain collection.
- Add-on "[Will these links block Tor user?](subfiles/addon/isat.md)" will tell you which link rejected Tor visitor.
- Search [anti-tor fqdn list](anti-tor_users/domains/).
  - Karma's ["Find Anti-Tor FQDN" API](subfiles/service/karma_api.md)

![](image/tor_nontor_diff.jpg)

- Some news websites are lying to Tor users. You can read their website if you are not using Tor nor VPN. If you visit their website over Tor, they just say "_Sorry, article not found_".

![](image/imunify360.jpg)

- [Imunify360](https://web.archive.org/web/20200617160904/https://www.imunify360.com/) is not so [intelligent](https://whc.ca/blog/introducing-imunify360-your-new-intelligent-firewall/) because it is blocking real human.

- Some famous mail subscription service and some ISP websites are displaying "Maintenance" page if you visit them over Tor.

**How can you trust their sites if they are not treating everyone equally?**

```
IMPORTANT: Please add full FQDN

    if "community.example.com" is blocking Tor user
        add "community.example.com"

    if "www.example.co.uk" is blocking Tor user
        add "www.example.co.uk"

    if "example.net" is blocking Tor user
        add "example.net"

... to antitor_e.txt
```

If your website is on this list, you better talk with your network administrator.

**But my website X no longer blocking Tor users!**

Are you sure? There are two ways to remove yourself.
First option is just _*remove* it from the list_ and _create a pull request_.
Second option is _wait 3 months_. Our system will revisit your website as a Tor user.

If you're not blocking Tor users you will be removed automatically.

- If your website is using Cloudflare
  - There's a higher chance that we receive rejection webpage from Cloudflare. Do not use cloudflare.

</details>

------

<details>
<summary><h3>How to add your data</h3></summary>

B or C will be enough. (or D if you really can't)
**Thank you for your contribution. You are doing a good job!**


> Type B: Push to git

1. Log in to [this website's Git](http://crimeflare.eu.org).
2. Click "*Fork*" button.  (top-left corner)
3. Edit `text` file.  (_you don't have to edit JSON file_)
4. Create a *new pull request*.


> Type C: Just scan the FQDN

Your contribution will be pushed to git automatically.

- Cloudflare
  - **Easiest way**: Use [**CfDomains report tool**](tool/cfdomains/README.md).
  - Or: Scan FQDN on "[Search domain](subfiles/service/ombrelo.md)" webpage.
  - Or: Use ["_MITM test_" API](subfiles/service/ombrelo.md).
    - e.g. `curl -x socks5h://127.0.0.1:9050 -k --http2 -X POST -F 'f=www.emsisoft.com' (API URL)is_mitm.php`


> Type D: Create an Issue

Create an Issue (you can also [contribute anonymously](README.md)) and let us know about the change you want to make.
You can add multiple URLs in one issue.

</details>

------

<details>
<summary><h3>How to setup git</h3></summary>

This procedure will give you a cloudflare-tor fork with a privacy-respecting configuration to do pushes with SSH over Tor using `git.example`.
Below procedure is designed for _Linux_.
The first step covers Windows too, but these instructions probably
need more adaptations for Windows and other platforms.

- Linux: `aptitude install git tor ssh`
- Windows: Download `PortableGit` from [Github](https://github.com/git-for-windows/) & run `git-bash.exe`

1. Install Git, SSH(Not Windows), and Tor (if you haven't already)
1. Create a `git.example` account (username "snowden" will be used for this example)
1. Create an SSH key pair `$ ssh-keygen -t rsa -N '' -C 'snowden at git' -f "$HOME"/.ssh/id_rsa_mrsnowden`
1. Edit `$HOME/.ssh/config`:

```
    host git.example
         hostname     git.example
         ForwardX11   no
         ProxyCommand connect -5 -S 127.0.0.1:9050 $(tor-resolve %h 127.0.0.1:9050) %p
    host mrsnowden
         IdentityFile /home/user/.ssh/id_rsa_mrsnowden
```

1. copy `"$HOME"/.ssh/id_rsa_mrsnowden.pub` to clipboard
1. git.example > settings > SSH/GPG Keys > add key (paste from clipboard)
1. $ `firefox https://git.example/deCloudflare/deCloudflare`
1. fork it (top right corner)
1. go to the directory you want the project to be rooted in (hereafter we'll call it `$project_root`).
1. anonymously download your fork: $ `git clone git@mrsnowden:you/cloudflare-tor.git`
1. edit `$project_root/cloudflare-tor/.git/config` to include the account name and email address that will be on every commit, as well as the URL:

```
[user]
        email = noreply@example.com
        name = snowden
[remote "origin"]
        url = git@mrsnowden:snowden/cloudflare-tor.git
     	fetch = +refs/heads/*:refs/remotes/origin/*
[remote "upstream"]
        url = git@mrsnowden:deCloudflare/deCloudflare.git
     	fetch = +refs/heads/*:refs/remotes/origin/*
[branch "master"]
	remote = origin
	merge = refs/heads/master
```

1. make your first change
1. (from `$project_root`) $ `git add . -u -n`
1. check that the files listed are what you changed and intend to push upstream
1. if yes: `$ git add . -u`
1. $ `git commit -m 'description of first change'`
1. $ `git push origin master`
1. $ `firefox https://git.example/deCloudflare/deCloudflare`
1. make a new pull request

&nbsp;

Whenever git operates on the cloudflare-tor project, all connections
to git are automatically over Tor with this configuration
(because the `url` in `.git/config` references the virtual host
`mrsnowden` in `~/.ssh/config`).

</details>

------

<details>
<summary><h3>About Cloudflare base domain list</h3>
</summary>

Our mission is clear - `stay away from Cloudflare`.

If the `subdomain.example.com` is cloudflared, we add `example.com` to the database. (`subdomain.example.com` is the sub-domain of `example.com`. Only `the owner` of `example.com` can create sub-domain)

Even if `whatever.example.com` is _not_ behind cloudflare we _will_ raise a warning, because the base domain `example.com` is `cloudflare user`.

`The owner` of `example.com` can enable Cloudflare to `whatever.example.com` at any time without user's notice. It can be done from `dash.cloudflare.com` webpage or hitting `Cloudflare API`. `The owner` is supporting `Cloudflare` and this is severe `security risk`.

Until `the owner` completely stop using Cloudflare service for `example.com`, we _do not_ remove `example.com` from the database.

There is `no exception`.

```
"amazonpayments.com"

$ getweb --headonly https://pages.amazonpayments.com/robots.txt

cf-cache-status: HIT
expect-ct: max-age=604800, report-uri="https://report-uri.cloudflare.com/cdn-cgi/beacon/expect-ct"
alt-svc: h2="cflare******.onion:443"; ma=86400; persist=1
server: cloudflare
cf-ray: ***
```

If `the owner` moved away from `cloudflare` **completely**, you are welcome to add `example.com` to the "[ex_cloudflare_users.md](cloudflare_users/ex_cloudflare_users.md)" - after checking `example.com` with online tool.


`Only a few Cloudflare user leave Cloudflare. False positive is uncommon.`

</details>

---

![](image/cfisnotanoption.jpg)
