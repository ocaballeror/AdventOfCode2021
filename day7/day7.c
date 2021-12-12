#include <stdio.h>
#include <stdlib.h>


int* read_input() {
    FILE* fp = fopen("input", "r");

    fseek(fp, 0, SEEK_END);
    size_t fsize = ftell(fp);
    fseek(fp, 0, SEEK_SET);

    int* numbers = malloc(fsize * sizeof(int));
    int* cursor = numbers;

    while(fscanf(fp, "%d,", cursor) != EOF) cursor++;
    *cursor = -1;

    fclose(fp);

    return numbers;
}


int max(int* arr) {
    int res = -1;

    for (int i=0; arr[i] != -1; i++){
        if(arr[i] > res) res = arr[i];
    }

    return res;
}

int min(int* arr) {
    int res = -1;

    for (int i=0; arr[i] != -1; i++){
        if(arr[i] < res || res == -1) res = arr[i];
    }

    return res;
}


int part1() {
    int* numbers = read_input();
    int start = min(numbers), end = max(numbers);
    int best = -1;

    for (int align=start; align<=end; align++){
        int sum = 0;
        for (int i=0; numbers[i] != -1; i++) {
            sum += abs(numbers[i] - align);
        }
        if(sum < best || best == -1) best = sum;
    }

    free(numbers);
    return best;
}

int part2() {
    int* numbers = read_input();
    int start = min(numbers), end = max(numbers);
    int best = -1;

    for (int align=start; align<=end; align++){
        int sum = 0;
        for (int i=0; numbers[i] != -1; i++) {
            for (int j=1; j<=abs(numbers[i] - align + 1); j++){
                sum += j;
            }
        }
        if(sum < best || best == -1) best = sum;
    }

    free(numbers);
    return best;
}

int main(){
    printf("Part 1: %d\n", part1());
    printf("Part 2: %d\n", part2());
    return 0;
}
