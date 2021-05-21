#include <vector>
#include "iostream"
using namespace std;

int main() {
    int h, w;
    cin >> h >> w;
    vector<string> s(h, "");
    for (int i=0; i < h; i++) {
        cin >> s[i];
    }
    for (auto a: s) {
        for (auto b: a) {
            cout << b << endl;
        }
    }
    return 0;
}
