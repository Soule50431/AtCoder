#include<bits/stdc++.h>
using namespace std;
#define rep(i, n) for (int i = 0; i < (n); ++i)
using ll=long long;
double inf = INFINITY;

int main() {
    int n, m;
    vector<vector<ll>> dist(n, vector<ll>(n, inf));
    cin >> n >> m;
    rep(i, n){
        int a, b, c;
        cin >> a >> b >> c;
        dist.at(a).at(b) = c;
    }

    return 0;
}
