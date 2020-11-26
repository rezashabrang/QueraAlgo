#include <iostream>
#include <cstring>

using namespace std;

int main() {

    // n
    int n;
    cin >> n;
    int array_numbers[n];
    // Getting Numbers
    for (int i = 0; i < n; i++) {
        cin >> array_numbers[i];
    }
    cout << array_numbers;
    return 0;
}