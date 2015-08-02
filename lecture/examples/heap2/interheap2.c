// Fedora 20 x64: gcc ./intraheap.c
struct goaty { char name[8]; int should_run_calc; };
 
int main(int argc, const char* argv[]) {
    struct goaty* g = malloc(sizeof(struct goaty));
    g->should_run_calc = 0;
    strcpy(g->name, "projectzero");
    if (g->should_run_calc) execl("/usr/bin/gnome-calculator", 0);
}
