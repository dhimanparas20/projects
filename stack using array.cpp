#include <iostream>
#include <stdlib.h>
using namespace std;
// STack follows LIFO (LAST IN FIRST OUT)
class Stack{
    int top=0;
    int arr[5];
    public:
    void push (int x){
        if (top == 5){
            cout<<"STACK OVERFLOW"<<endl;
            return ; 
        }
        else{
        arr[top]=x;
        top +=1;
    }
    }
    void pop(){
        if (top == 0){
            cout<<"STACK UNDERFLOW"<<endl;
            return ; 
        }
        else{
        cout<<"Popped element :" <<arr[top-1]<<endl;
        arr[top-1]=NULL;
        top -=1;
    }
    }
    void display(){
        cout<<"Elements of stack are:"<<endl;
        for (int i=top-1;i>=0;i--){
            cout<<arr[i]<<endl;
        }
    }
};
int main(){
    Stack s1;
    int opt,no;
    while (true){
    cout<<"--------------------------------------------"<<endl;    
    cout<<"1. To PUSH element to stack."<<endl;
    cout<<"2. To POP element from stack."<<endl;
    cout<<"3. To display elements of stack."<<endl;
    cout<<"4. To EXIT"<<endl;
    cout<<"--------------------------------------------"<<endl;
    cout<<"Enter Your Choice: ";
    cin>>opt;
    system("clear");
    cout<<"--------------------------------------------"<<endl;
    switch(opt){
        case 1:
        cout<<"Enter the element to push: ";
        cin>>no;
        s1.push(no);
        break;
        
        case 2:
        s1.pop();
        break;
        
        case 3:
        s1.display();
        break;
        
        case 4:
        cout<<"im called";
        exit(0);
    }
}
cout <<"CODE EXIT";
return 0;
}
