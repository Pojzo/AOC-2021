#include <stdlib.h>
#include <iostream>
#include <string.h>

const std::string forward = "forward";
const std::string down = "down";
const std::string up = "up";

int main() {
    int horizontal_pos = 0;
    int depth = 0;
    std::string command;
    int value;
    while (std::cin >> command && std::cin >> value) {
        if (command == forward) {
            horizontal_pos += value;
        }
        else if (command == down) {
            depth += value;
        }
        else {
            depth -= value;
        }
    }
    std::cout << "Result: " << depth * horizontal_pos << std::endl;
    
    return 0;
}
