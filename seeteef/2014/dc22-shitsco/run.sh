#!/bin/sh
socat tcp-l:31337,reuseaddr,fork exec:"./shit"
#socat tcp-l:31337,reuseaddr,fork exec:"strace -ifx ./shit"
