#include<iostream>
#include <cmath>
using namespace std;

class Distance{
    public:
    int f;
    float i;
    float temp;
    Distance(){
        f = 0;
        i = 0.0;
    }
    Distance(int feet,float inch){
        f = feet ;
        i = inch;
    }
    Distance operator +(Distance obj){
        Distance temp;
        float xi;
        int yf;
        xi = i +obj.i;   // for inches
        yf = f +obj.f;   // for feets
        if (xi>=12){
            temp.f = yf+(xi/12);
            temp.i = std::fmod(xi, 12.0);
        }
        else{
            temp.f = yf;
            temp.i = xi;
        }
        return temp;
    } 
    void display(){
        cout<<"Final Feet = "<<f<<endl;
        cout<<"Final Inches = "<<i;
    }
    
};

int main(){
    int feet;
    float inch;
    Distance d1(11,40.0),d2(19,56.0),d0;
    d0 = d1+d2;
    d0.display();
    return 0;
}
