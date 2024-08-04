#include <iostream>
using namespace std;
string s;
int len;
int main()
{
    cin>>s;
    len=s.length();
    for(int i=0;i<len/2;i++){
        if(s[i]!=s[len-1-i]){
            cout<<0;
            return 0;
        }
    }
    cout<<1;
}