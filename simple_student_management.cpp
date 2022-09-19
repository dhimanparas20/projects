#include <iostream>
#include<string.h>
using namespace std;

class Student{
  int roll;
  float cgpa;
  string name;

  public:
  void set_data();
  void show_data();
};

int main(){
  int i,j;
  Student obj[50];
  cout<<"Enter the total no of students(<50): ";
  cin>>j;
  for(i=0;i<j;i++){
  obj[i].set_data();
  }
  for(i=0;i<j;i++){
  obj[i].show_data();
  }
  return 0;
}

void Student::set_data(){
  cout<<"Enter Name of the student: ";
  cin>>name;
  cout<<"Enter Roll No of Student: ";
  cin>>roll;
  cout<<"Enter CGPA: ";
  cin>>cgpa;
}

void Student::show_data(){
  cout<<"\n--------------------------------------------"<<endl;
  cout<<"Name: " <<name <<endl;
  cout<<"Roll No." <<roll <<endl;
  cout<<"CGPA :" <<cgpa <<endl;
  cout<<"\n--------------------------------------------"<<endl;
}
