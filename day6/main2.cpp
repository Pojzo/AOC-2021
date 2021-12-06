#include <iostream>
#include <sstream>
#include <vector>
#include <algorithm>

long long simulate(std::vector<int> ocean, int num_days);

void vector_print(std::vector<long long> v) {
    for (auto i : v) {
        std::cout << i << " ";
    }
    std::cout << std::endl;
}

long long vector_sum(std::vector<long long> v) {
    long long sm = 0;
    for (auto i : v) {
        sm += i;
    }
    return sm;
}

int main(int argc, char **argv) {
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

    std::cout << "Number of fish after " << atoi(argv[1]) + 1<< ": " << simulate(ocean, atoi(argv[1])) << std::endl;
    return 0;
}

// return number of fish after NUM_DAYS days

long long simulate(std::vector<int> ocean, int num_days) {
    long long count = 0;
    std::vector<long long> arr(9, 0);
    for (int i = 0; i < ocean.size(); i++) {
        arr[ocean[i]] += 1;
    }
    vector_print(arr);
    long long num_zeros;
    long long current, prev;
    for (int i = 0; i < num_days; i++) {
        num_zeros = arr[0];
        current = arr[8];
        for (int i = 7; i >= 0; i--) {
            prev = arr[i];
            arr[i] = current;
            current = prev;
        }
        arr[6] += num_zeros;
        arr[8] = num_zeros;
        vector_print(arr);
    }
    return vector_sum(arr);
}
