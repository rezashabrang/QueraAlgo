#include <iostream>

using namespace std;

int main() {
    long int mod = 1.0e9 + 7;
    int q;
    int ans;
    // Getting q
    cin >> q;
    int *questions = new int[q];
    // brick function
    long long int brick[static_cast<int>(1e5 - 3)];
    // Getting Questions
    for (int i = 0; i < q; i++)
        cin >> questions[i];
    brick[0] = 1;
    brick[1] = 1;
    brick[2] = 1;
    brick[3] = 2;
    for (int i = 4; i <= 1.0e5; i++)
        brick[i] = brick[i - 1] + brick[i - 2] + brick[i - 3] + brick[i - 4];
    for (long long int i = 0; i < q; i++) {
        ans = brick[questions[i]];
        cout << ans << endl;
    }


}
