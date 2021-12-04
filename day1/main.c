#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

int main() {
    FILE *fp = fopen("input", "r");
    char buffer[10];
    bool first = true;
    int previous, current;
    int count = 0;
    while (fgets(buffer, 10, fp)) {
        if (first) {
            previous = atoi(buffer);
            current = previous;
            first = false;
        }
        else {
            previous = current;
            current = atoi(buffer);
            if (current > previous) {
                count++;
            }
        }
    }
    printf("%d\n", count);
}

