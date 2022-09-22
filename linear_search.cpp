#include<iostream>
using namespace std;

void get_data(int len,int arr[]){
  for (int i=0;i<len;i++){
    cout<<"Enter the value of element "<<i+1<<": ";
    cin>>arr[i];
  }}

void show_data(int len,int arr[]){
  for(int i=0;i<len;i++){
    cout<<arr[i]<<endl;
  }
} 

int look(int len,int num,int arr[]){
  for(int i=0;i<len;i++){
    if (num == arr[i]){
      return i+1;
    }
  }
  return -1;
}

int main(){ 
  int len,num;
  cout<<"Enter the size of array: ";
  cin>> len;
  int arr[len];
  cout<<endl;
  get_data(len,arr);
  cout<<"\nThe members of the array are:\n";
  cout<<"------------------------------------------------------\n";
  show_data(len,arr);
  cout<<"------------------------------------------------------\n\n";
  cout <<"Enter the number u want to search in array :";
  cin>>num;
  if (look(len,num,arr) !=  -1){
    cout<<"Element "<<num<<" found at" <<look(len,num,arr)<<endl;
  }
  else{
    cout<<"Element "<<num<<" not found"<<endl; 
  }
  return 0;
}
