#!/bin/sh

valgrind --tool=callgrind --instr-atstart=yes --dump-instr=no --simulate-cache=no --collect-jumps=yes $1 $1

# kcachegrind <file>
