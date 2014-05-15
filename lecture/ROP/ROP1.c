#include <stdio.h>
#include <stdlib.h>
#include <errno.h>
#include <string.h>
#include <sys/types.h>
#include <netinet/in.h>
#include <sys/socket.h>
#include <sys/wait.h>
#include <pwd.h>
#include <fcntl.h>
#include <signal.h>

#define PORT 31337
#define BACKLOG 10
#define BUFSIZE 1024
#define DEBUG 0

struct sockaddr_in my_addr;
struct sockaddr_in their_addr;
int sin_size;
int svr_fd, cli_fd;

int SetupSocket()
{
    int sockfd;

    if ((sockfd = socket (AF_INET, SOCK_STREAM, 0)) == -1) {
        perror ("socket");
        exit (1);
    }

    my_addr.sin_family = AF_INET;
    my_addr.sin_port = htons (PORT);
    my_addr.sin_addr.s_addr = INADDR_ANY;
    bzero (&(my_addr.sin_zero), 8);

    int option = 1;
    setsockopt (sockfd, SOL_SOCKET, SO_REUSEADDR, &option, sizeof (int));

    if (bind (sockfd, (struct sockaddr *) &my_addr, sizeof (struct sockaddr)) == -1) {
        perror ("bind");
        exit (1);
    }

    if (listen (sockfd, BACKLOG) == -1) {
        perror ("listen");
        exit (1);
    }

    return sockfd;
}

int send_data(int fd, char *msg, int p_numofBytes)
{
    int nReadByte = 0;
    int n = 0;
    char *sendMsg = msg;

    while (nReadByte < p_numofBytes) {
        n = send(fd, (char *) sendMsg + nReadByte, p_numofBytes - nReadByte, 0);
        nReadByte += n;
        if (n < 0) {
            return -1;
        }
    }

    return nReadByte;
}

int send_string(int fd, char *msg)
{
    return send_data(fd, msg, strlen (msg));
}

int recv_data(int fd, char *buf, int nReadBytes)
{
    int cnt = 0;
    int rv = -1;

    while (cnt < nReadBytes && rv)
    {
        rv = recv(fd, (char *) buf + cnt, 1, 0);
        if (buf[cnt] == '\n') {
            return cnt;
        }

        if (rv < 0) {
            return -1;
        }
        ++cnt;
    }

    return cnt;
}

void socket_flush (int fd)
{
    int nread = -1;
    char c;
    while ((nread = read (fd, &c, 1, 0)) > 0) {
        printf("cleaning...: %c\n", c);
        continue;
    }
}

int question(int fd)
{
    char buf[16];
    int rv = -1;
    int f = fd;
    int i = 0;
    send_string(f, "What is your name: ");
    rv = recv_data(f, buf, BUFSIZE+128);
    rv = send_data(f, buf, rv+16);
    return rv;
}

int handler(int fd)
{
    int rv = -1;
    int fb = -1;

    rv = question(fd);
    close(fd);
    return rv;
}

void accept_loop(fd)
{
    int pid;
    int status;
    int rv = -1;

    signal(SIGCHLD, SIG_IGN);

    // infinite loop
    while ( 1 ) {
        sin_size = sizeof (struct sockaddr_in);
        if ((cli_fd = accept (fd, (struct sockaddr *) &their_addr, &sin_size)) == -1) {
            perror ("accept");
            continue;
        }

        printf("Verbose: connected from %s\n", (char *)inet_ntoa(their_addr.sin_addr));

        pid = fork ();
        if ( !pid ) {
            close(svr_fd);
            status = handler(cli_fd);
            exit(status);
        } else {
            close(cli_fd);
        }
    }
}

int main(int argc, char **argv)
{
    svr_fd = SetupSocket();
    accept_loop(svr_fd);
    return svr_fd;
}
