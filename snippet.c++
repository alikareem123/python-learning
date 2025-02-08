#include <iostream>
#include <map>
using namespace std;

int main() {
	// your code goes here
    int t;
    cin>>t;
    while(t--){
        int n;
        cin>>n;
        map<int, int> m;
        for(int i = 0; i < n; i++){
            int k;
            cin>>k;
            m[k]++;
        }
        for(auto i: m){
            if(i.second % 2 != 0){
                cout<<i.first<<endl;
            }
        }
    }
}