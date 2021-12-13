#include <stdio.h>
#include <stdlib.h>

char* read_input() {
    FILE* fp = fopen("input", "r");
    if(!fp) {
        perror("Cannot read input");
        exit(1);
    }

    fseek(fp, 0, SEEK_END);
    size_t fsize = ftell(fp);
    fseek(fp, 0, SEEK_SET);

    char* content = malloc(fsize + 1);
    fread(content, fsize, 1, fp);
    content[fsize] = '\0';

    fclose(fp);

    return content;
}

int part1() {
    char* lines = read_input();

    free(lines);

    return 0;
}

int part2() {
    char* lines = read_input();

    free(lines);

    return 0;
}

int main(){
    printf("Part 1: %d\n", part1());
    printf("Part 2: %d\n", part2());

    return 0;
}
