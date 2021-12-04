#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

int main() {
    FILE *fp = fopen("input", "r");
    char buffer[10];
    int line_count = 0;
    int first, second, third;
    int previous_sum, current_sum;
    previous_sum = current_sum = 0;
    int count = 0;
    while (fgets(buffer, 10, fp)) {
        ++line_count;
        if (line_count == 1) {
            first = atoi(buffer);
        }
        else if (line_count == 2) {
            second = atoi(buffer);
        }
        else if (line_count == 3){
            third = atoi(buffer);
            previous_sum = first + second + third;
            current_sum = previous_sum;
        }
        else {
            current_sum -= first;
            first = second;
            second = third;
            third = atoi(buffer);

            current_sum += third;
            if (current_sum > previous_sum) {
                ++count;
            }
            previous_sum = current_sum;
        }
             
    }
    printf("%d\n", count);
}
