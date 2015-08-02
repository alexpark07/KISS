// Fedora 20 x64: gcc -fstack-protector ./stack.c
void subfunc() {
    char buf[8];
    buf[16] = 1;
}
 
int main() {
    int run_calc = 0;
    printf("before stack smashing\nrun_calc: %d\n", run_calc);
    subfunc();
    printf("after stack smashed\nrun_calc: %d\n", run_calc);
    if (run_calc) execl("/usr/bin/gnome-calculator", 0);
}
