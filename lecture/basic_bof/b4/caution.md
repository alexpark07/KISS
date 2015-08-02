``` 
 # ASLR 끄기
 # sysctl -w kernel.randomize_va_space=0 

 # read 주소 찾기

 # ASLR일 경우
 # grep -d libc.so.6 | grep "read>:" 

 # ASLR이 아닐 경우
 # gdb bof4
 # start
 # print read

 # BSS (쓰기 가능한 주소 찾는 방법)
 # cat /proc/`pidof bof4`/maps
 # cat /proc/[process id]/maps 
 # rw 권한이 부여된 곳의 주소를 찾음
```

