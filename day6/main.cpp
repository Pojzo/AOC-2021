#include <iostream>
#include <sstream>
#include <vector>

const int NUM_DAYS = 79;

int simulate(std::vector<int> ocean);

int main() {
    std::vector<int> ocean;
    std::string str;
    getline(std::cin, str);
    std::stringstream ss;
    ss << str;
    while (ss.good()) {
        std::string substr;
        getline(ss, substr, ',');
        ocean.push_back(atoi(substr.c_str()));
    }

    std::cout << "Number of fish after " << NUM_DAYS + 1<< ": " << simulate(ocean) << std::endl;
    return 0;
}

// return number of fish after NUM_DAYS days
int simulate(std::vector<int> ocean) {
    for (int i = 0; i < NUM_DAYS; i++) {
        int size = ocean.size();
        for (int j = 0; j < size; j++) {
            ocean[j] -= 1;
            if (ocean[j] == 0) {
                ocean[j] = 7;
                ocean.push_back(9);
            }
        }
    }
    return ocean.size();
}
