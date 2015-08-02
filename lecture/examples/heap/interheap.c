// Fedora 20 x64: gcc ./interheap.c; n=0; while true; do ./a.out; done
int main(int argc, const char* argv[]) {
    void* ptrs[1024];
    int i;
    void* ptr1;
    int *run_calc;
    int seed = (argc > 1) ? atoi(argv[1]) : getpid();
    srandom(seed); printf("seed: %d\n", seed);  // ./a.out 21526 pops.
    for (i = 0; i < 1024; ++i) ptrs[i] = malloc(random() % 1024);
    for (i = 0; i < 1024; ++i) if (random() % 2) free(ptrs[i]);
    ptr1 = malloc(128); run_calc = malloc(128);
    *run_calc = 0;
    memset(ptr1, 'A', 4096);
    if (*run_calc) execl("/usr/bin/gnome-calculator", 0);
}
