#include <iostream>
#include <chrono>

int main() {
    auto start = std::chrono::high_resolution_clock::now();

    for (long long i = 0; i < 1'000'000'000; i++);

    auto end = std::chrono::high_resolution_clock::now();
    std::chrono::duration<double> duration = end - start;

    std::cout << "Waktu eksekusi: " << duration.count() << " detik\n";
    return 0;


}