#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <limits.h>

const int sample_len = 10;
const int input_len = 1000;

long long calculate_fuel(int *arr, int len, int position) {
    long long sm = 0;
    for (int i = 0; i < len; i++) {
        sm += abs(arr[i] - position);
    }
    return sm;
}

void solution(int *arr, int len);

int main() {
    const int len = input_len;
    int *arr = (int *) malloc(len * sizeof(int));
    int cur;
    char temp;
    for (int i = 0; i < len; i++) {
        scanf("%d", &cur);
        scanf("%c", &temp);
        arr[i] = cur;
    }
    solution(arr, len);
    return 0;
}

void solution(int *arr, int len) {
    long long min_fuel = INT_MAX;
    long long cur_fuel;
    int min_pos;
    for (int i = 0; i < len + 1; i++) {
        cur_fuel = calculate_fuel(arr, len, i);
        if (cur_fuel < min_fuel) {
            min_fuel = cur_fuel;
            min_pos = i;
        }
    }
    printf("Minimum fuel: %lld\nPosition: %d\n", min_fuel, min_pos);
}

