# socat / nc / xinetd를 이용한 standalone binary 실행하기

```
  CTF/Wargame 바이너리 중 네트워크 기능이 없는 문제인데 리모트 pwnable인 경우가 있다.
  이 경우는 10중 8~9는 socat/ xinetd/ netcat 등으로 socket binding을 이용한다. 
```

## socat 방법

*local test*

```
alex@ubuntu:~/hack/CTF_Code/shellcode$ shellcraft cat ./flag -f r | ./demo -
Read 57 bytes of shell code. Here goes.
~~~ Running shellcode ~~~
The flag is: 54f6ea7093d2582f6b32ed396c048c8a
Segmentation fault
```

*remote test*

```
### alex@ubuntu:~/hack/CTF_Code/shellcode$ cat run.sh 

#!/bin/sh
socat TCP-LISTEN:31337,reuseaddr,fork EXEC:"$1"
```
  실행
  
``./run.sh "./demo -"``

  공격
  
``shellcraft cat ./flag -f r | nc localhost 31337``

```
결과: 
alex@ubuntu:~$ shellcraft cat ./flag -f r | nc localhost 31337
The flag is: 54f6ea7093d2582f6b32ed396c048c8a
```

-----

## netcat 방법

```
실행:
alex@ubuntu:~/hack/CTF_Code/shellcode$ while [ 1 ]; do nc.traditional -c "./demo -" -lp 31337 -v ; done
listening on [any] 31337 ...
connect to [127.0.0.1] from localhost [127.0.0.1] 59192
Segmentation fault
```

```
결과:
alex@ubuntu:~$ shellcraft cat ./flag -f r | nc localhost 31337
The flag is: 54f6ea7093d2582f6b32ed396c048c8a
```

-----

## xinetd 방법

```
실행:

# in /etc/xinet.d/ctf31337 file

root@ubuntu:~# cat /etc/xinetd.d/ctf31337 

service ctf31337
{
    disable = no
    socket_type = stream
    flags = REUSE
    protocol = tcp
    wait = no
    user = ctf
    server = /home/ctf/demo
    server_args = "-"
    log_on_failure += USERID
}

# in /etc/services file

root@ubuntu:~# grep ctf31337 /etc/services 
ctf31337   31337/tcp          # ctf binary

# netstat -an
root@ubuntu:~# netstat -anpt | grep 31337
tcp        0      0 0.0.0.0:31337           0.0.0.0:*               LISTEN      4824/xinetd

```

```
결과:
alex@ubuntu:/home/ctf$ shellcraft cat /home/ctf/flag -f r | nc localhost 31337
7b73d184b117905905e6398fcb6a5dd6
```

## socat - port forwarding

```
socat TCP-LISTEN:80,fork TCP:destination_ip_address:80
```
