#include <stdio.h>
#include <stdlib.h>

int part2(){
    FILE* fp = fopen("input", "r");
    if(!fp) {
        perror("Cannot read input");
        exit(1);
    }
    int count = 0;
    int read, read_count = 0;
    int window[3] = {0, 0, 0};
    int window_sum = 0, new_window_sum;
    while(!feof(fp)) {
        fscanf(fp, "%d", &read);
        read_count++;
        new_window_sum = window_sum + read - window[0];
        if(read_count > 3 && new_window_sum > window_sum) {
            count++;
        }
        window_sum = new_window_sum;

        window[0] = window[1];
        window[1] = window[2];
        window[2] = read;
    }
    fclose(fp);
    return count;
}

int part1() {
    FILE* fp = fopen("input", "r");
    if(!fp) {
        perror("Cannot read input");
        exit(1);
    }
    int read, last = -1, count = 0;
    while(!feof(fp)) {
        fscanf(fp, "%d", &read);
        if(last != -1 && read > last) count++;
        last = read;
    }
    fclose(fp);
    return count;
}


int main(){
    printf("Part 1: %d\n", part1());
    printf("Part 2: %d\n", part2());
    return 0;
}
