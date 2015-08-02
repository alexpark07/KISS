// Fedora 20 x64: gcc ./uaf.c
struct unicorn_counter { int num; };
 
int main() {
    struct unicorn_counter* p_unicorn_counter;
    int* run_calc = malloc(sizeof(int));
    *run_calc = 0;
    free(run_calc);
    p_unicorn_counter = malloc(sizeof(struct unicorn_counter));
    p_unicorn_counter->num = 42;
    if (*run_calc) execl("/usr/bin/gnome-calculator", 0);
}
