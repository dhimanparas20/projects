#include <iostream>
#include <stdlib.h>
using namespace std;
// Queue follows FIFO (FIRST IN FIRST OUT)
class Stack{
    int rear=0,front=0;
    int arr[5];
    public:
    void enq (int x){
        if (rear == 5){
            cout<<"QUEUE OVERFLOW"<<endl;
            return ; 
        }
        else{
        arr[rear]=x;
        rear +=1;
    }
    }
    void deq(){
        if (rear == front){
            cout<<"QUEUE UNDERFLOW"<<endl;
            return ; 
        }
        else{
        cout<<"Popped element :" <<arr[front]<<endl;
        arr[front]=NULL;
        front +=1 ;
    }
    }
    void display(){
        cout<<"Elements of Queue are:"<<endl;
        for (int i=front;i<rear;i++){
            cout<<arr[i]<<" | ";
        }
        cout<<endl;
    }
};
int main(){
    Stack s1;
    int opt,no;
    while (true){
    cout<<"--------------------------------------------"<<endl;    
    cout<<"1. To enter element to queue."<<endl;
    cout<<"2. To delete element from queue."<<endl;
    cout<<"3. To display elements of queue."<<endl;
    cout<<"4. To EXIT"<<endl;
    cout<<"--------------------------------------------"<<endl;
    cout<<"Enter Your Choice: ";
    cin>>opt;
    system("clear");
    cout<<"--------------------------------------------"<<endl;
    switch(opt){
        case 1:
        cout<<"Enter the element in queue: ";
        cin>>no;
        s1.enq(no);
        break;
        
        case 2:
        s1.deq();
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
