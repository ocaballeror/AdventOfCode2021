#include <stdio.h>
#include <stdlib.h>


void incr_window(int* window, int* window_count, int value) {
    if(*window_count < 0) {}
    else if(*window_count == 0) {
        *window = value;
    } else if(*window_count < 3) {
        *window += value;
    }

    // cannot use mod here bc it would screw negative values
    (*window_count)++;
    if(*window_count > 3) {
        *window_count = 0;
    }
}

int part2(){
    FILE* fp = fopen("input", "r");
    if(!fp) {
        perror("Cannot read input");
        exit(1);
    }
    int count = 0;
    int read;
    int window1 = 0, window2 = 0, window3 = 0, window4 = 0;
    int window1_count = 0, window2_count = -1, window3_count = -2, window4_count = -3;
    while(!feof(fp)) {
        fscanf(fp, "%d", &read);
        incr_window(&window1, &window1_count, read);
        incr_window(&window2, &window2_count, read);
        incr_window(&window3, &window3_count, read);
        incr_window(&window4, &window4_count, read);
        if(window1_count == 0 && window2_count == 3 && window2 > window1)
            count++;
        else if(window2_count == 0 && window3_count == 3 && window3 > window2)
            count++;
        else if(window3_count == 0 && window4_count == 3 && window4 > window3)
            count++;
        else if(window4_count == 0 && window1_count == 3 && window1 > window4 && window4 > 0)
            count++;

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
