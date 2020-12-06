#include <iostream>
#include <cmath>
#include <algorithm>

using namespace std;

int main() {
    // lowest number possible
    int a;
    long double ans = -1.0e100;
    // n
    long int n;
    cin >> n;
    int *array_numbers = new int[n];
    // Getting Numbers
    for (int i = 0; i < n; i++) {
        cin >> array_numbers[i];
    }
    //end of processing input
    int *maximimsum = new int[n];
    maximimsum[0] = array_numbers[0];
    for (int i = 1; i < n; i++)
        maximimsum[i] = fmax(array_numbers[i], array_numbers[i] + maximimsum[i - 1]);
    for (int i = 1; i < n; i++)
        ans = fmax(ans, maximimsum[i]);
    cout << ans << endl;
    return 0;
}