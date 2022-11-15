#include<iostream>
using namespace std;

class Matrix{
    public:
    int a[4][4];
    
    void get_matrix(){
        for(int i=1;i<=3;i++){
            for(int j=1;j<=3;j++){
                cout<<"Enter the value of elemenmt at position "<<i<<" "<<j<<": ";
                cin>>a[i][j];
                if(j==3){
                    cout<<endl;
                }
                
            }
        }
    }
    void display(){
        cout<<"\nThe 3x3 Matrix is as follows:\n";
        for(int i=1;i<=3;i++){
            for(int j=1;j<=3;j++){
                cout<<"| "<<a[i][j]<<" "<<"|";
                if(j==3){
                    cout<<endl;
                }
            } 
        }
    } 
    void inverse(){
        cout<<"\nThe inversed 3x3 Matrix is as follows:\n";
        for(int i=1;i<=3;i++){
            for(int j=1;j<=3;j++){
                cout<<"| "<<a[j][i]<<" "<<"|";
                if(j==3){
                    cout<<endl;
                }
            } 
        }
        
    }
};

int main(){
    Matrix a;
    a.get_matrix();
    a.display();
    a.inverse();
    return 0;
}
