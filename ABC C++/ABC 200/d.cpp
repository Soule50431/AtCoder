#include<bits/stdc++.h>
using namespace std;
#define rep(i, n) for (int i = 0; i < (n); ++i)

void output(int x) {
    vector<int> a;
//    cout << x << endl;
    int i = 1;
    while (x) {
        if (x&1) a.push_back(i);
        i++;
        x >>= 1;
    }
    cout << a.size();
    for (int x :a) cout << " " << x;
    cout << endl;
}


int main() {
    int n;
    cin >> n;
//    printf("%d", n);
    vector<int> a(n);
    rep(i, n) cin >> a[i];
    n = min(n, 8);

    vector<int> mod(200, 0);

    for (int i=0; i<(1<<n); i++) {
        int x = 0;
        for (int j=0; j<n; j++) {
            if ((i>>j)&1) x = (x + a[j]) % 200;
        }
//        cout << x << endl;
        if (mod[x] == 0) mod[x] = i;
        else {
            cout << "Yes" << endl;
            output(i);
            output(mod[x]);
            return 0;
        }
    }
    cout << "No" << endl;
    return 0;
}
