#include <iostream>
using namespace std;

int n=0,arr[100],v,cnt=0;
int main() 
{
    cin>>n;
    for(int i=0;i<n;i++){
        cin>>arr[i];
    }
    cin>>v;
    for(int i=0;i<n;i++){
        if(arr[i]==v){
            cnt+=1;
        }
    }
    cout<<cnt;
}