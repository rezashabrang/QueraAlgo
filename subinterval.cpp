#include <iostream>
#include <cstring>

using namespace std;

int main() {

    // n
    int n;
    cin >> n;
    int* array_numbers = new int[n];
    // Getting Numbers
    for (int i = 0; i < n; i++) {
        cin >> array_numbers[i];
    }
    for (int i = 0; i < n; i++) {
        cout << array_numbers[i]<<endl;
    }
    return 0;
    //test
}