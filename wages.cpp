#include <iostream>
using namespace std;
class Employee{
    int age;
    char name[10];
    public:
    int pay,base,rate;
    virtual void compute_pay() = 0;  //Pure Virtual Function
    void get_value(int rate, string pb){
        cout<<"Enter no of "<<pb<<" put per month: ";
        cin>>base;
        pay = base*rate;
    }
    void get_data(){
        cout<<"Enter your name: ";
        cin>>name;
        cout<<"Enter your age: ";
        cin>>age;
    }
    void show_data(){
        cout<<"\n--------------------------------------"<<endl;
        cout<<"Name: "<<Employee::name<<endl;
        cout<<"Age: "<<age<<endl;
        cout<<"Pay: "<<pay<<endl;
    }
    void set_main(int a,string b){
        if (a == -1 && b == "fixed"){pay = 50000; }
        else{get_value(a,b);}
        get_data();
        show_data();
    }
};
class wageEmployee:public Employee{
    public:
    void compute_pay(){
        set_main(50,"Hours");
    }
};

class regularEmployee:public Employee{
    public:
    void compute_pay(){
        set_main(-1,"fixed");
    }
};

class outsourceEmployee: public Employee{
    public:
    int work_days;
    void compute_pay(){
        set_main(400,"Days");
    }
};

int main(){
    int value,age,base;
    char name[15];
    wageEmployee we;
    regularEmployee re;
    outsourceEmployee oe;
    while (true){
        cout<<"\n--------------------------------------"<<endl;
        cout<<"1. For Daily Waged worker"<<endl;
        cout<<"2. For Regular Employee"<<endl;
        cout<<"3. For Outsource Employee"<<endl;
        cout<<"4. Exit"<<endl;
        cout<<"--------------------------------------"<<endl;
        cout<<"ENTER YOUR CHOICE: ";
        cin>>value;
        if (value == 4){
            exit(1);
        }
        cout<<"--------------------------------------"<<endl;
        switch(value){
            case 1:
              we.compute_pay();
              break;
            case 2:
              re.compute_pay();
              break;
            case 3:
              oe.compute_pay(); 
              break;  
            default:
              cout<<"Wrong choice entered";
        }
    }
return 0;
}     