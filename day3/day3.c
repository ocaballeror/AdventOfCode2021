#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>
#include <math.h>


int arrlen(void** arr) {
    int len = 0;
    while(arr[len] != NULL) len++;
    return len;
}

void arrfree(void** arr) {
    for(int i=0; arr[i] != NULL; i++) free(arr[i]);
    free(arr);
}

char** read_input() {
    FILE* fp = fopen("input", "r");
    if(!fp) {
        perror("Cannot read input");
        exit(1);
    }

    char first[64];
    fscanf(fp, "%s\n", first);
    int len = strlen(first);
    fseek(fp, 0, SEEK_END);
    size_t fsize = ftell(fp);
    int lines = ceil((double)fsize / (len + 1));
    char** numbers = malloc((lines + 1) * sizeof(char*));

    fseek(fp, 0, SEEK_SET);
    for(int i=0; i<lines; i++) {
        numbers[i] = malloc(len + 1);
        fgets(numbers[i], len+1, fp);
        fgetc(fp);  // consume newline
    }
    numbers[lines] = NULL;
    fclose(fp);

    return numbers;
}

int part1() {
    char** numbers = read_input();
    char bit;

    int len = strlen(numbers[0]);
    int lines = arrlen((void**)numbers);

    char* mode = malloc(len + 1);
    mode[len] = '\0';
    for(int offset=0; offset<len; offset++) {
        int ones = 0;
        for(int lineno=0; numbers[lineno] != NULL; lineno++) {
            bit = numbers[lineno][offset];
            if(bit == '1') ones++;
        }
        mode[offset] = ones >= lines/2? '1' : '0';
    }

    int gamma = strtol(mode, NULL, 2);
    int epsilon = (1 << len) - 1 - gamma;

    free(mode);
    arrfree((void**) numbers);

    return gamma * epsilon;
}

int filter(char** numbers, bool highest) {
    char bit;
    int len = strlen(numbers[0]);
    int lines = arrlen((void**) numbers);
    bool* valid = malloc(lines * sizeof(bool));
    memset(valid, true, lines);
    int valid_count = lines;
    int last_valid = 0;

    for(int offset=0; offset<len; offset++) {
        if(valid_count == 1) break;

        int ones = 0;
        for(int lineno=0; lineno<lines; lineno++) {
            if(!valid[lineno]) continue;

            bit = numbers[lineno][offset];
            if(bit == '1') ones++;
        }

        char mode = (highest ^ (ones * 2 >= valid_count)) + 48;
        for(int lineno=0; lineno<lines; lineno++) {
            if(!valid[lineno]) continue;

            if (numbers[lineno][offset] != mode) {
                valid[lineno] = false;
                valid_count--;
            } else {
                last_valid = lineno;
            }
        }
    }

    free(valid);
    return strtol(numbers[last_valid], NULL, 2);
}

int part2() {
    char** numbers = read_input();

    int oxy_rating = filter(numbers, true);
    int co2_rating = filter(numbers, false);

    arrfree((void**) numbers);

    return oxy_rating * co2_rating;
}

int main() {
    printf("Part 1: %d\n", part1());
    printf("Part 2: %d\n", part2());
    return 0;
}
