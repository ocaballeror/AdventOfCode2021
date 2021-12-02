#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int part1() {
    FILE* fp = fopen("input", "r");
    if(!fp) {
        perror("Cannot read input");
        exit(1);
    }

    char direction[32];
    int move;
    int depth = 0, forward = 0;
    while(!feof(fp)) {
        fscanf(fp, "%s %d\n", direction, &move);
        if(!strcmp(direction, "forward")) 
            forward += move;
        else if(!strcmp(direction, "down")) 
            depth += move;
        else if(!strcmp(direction, "up")) 
            depth -= move;
    }
    fclose(fp);

    return depth * forward;
}

int part2() {
    FILE* fp = fopen("input", "r");
    if(!fp) {
        perror("Cannot read input");
        exit(1);
    }

    char direction[32];
    int move;
    int depth = 0, forward = 0, aim = 0;
    while(!feof(fp)) {
        fscanf(fp, "%s %d\n", direction, &move);
        if(!strcmp(direction, "forward")) {
            forward += move;
            depth += aim * move;
        }
        else if(!strcmp(direction, "down")) {
            aim += move;
        }
        else if(!strcmp(direction, "up")) {
            aim -= move;
        }
    }
    fclose(fp);

    return depth * forward;
}

int main(){
    printf("Part 1: %d\n", part1());
    printf("Part 2: %d\n", part2());
	return 0;
}
