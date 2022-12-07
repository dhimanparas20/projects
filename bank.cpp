#include <iostream>
#include <fstream>
//#include <iomanip>
using namespace std;
class Account{  //Creating class ACCOUNT
    long int accNo;
    int accBal;
    char accName[20],accType[10];
public:
    void createAccount(){  //Creates Account
        cout<<"---------------------------------------";
        cout<<"\nEnter your name: ";
        cin>>accName;
        cout<<"Enter Account Number: ";
        cin>>accNo;
        cout<<"Enter Account Type (saving/current): ";
        cin>>accType;
        cout<<"Enter Account Balance: ";
        cin>>accBal;
    }
    void showAccount(){  //Displays Account Details
        cout<<"\nAccount Holder's Name: "<<accName<<endl;
        cout<<"Account Holder's Account Number: "<<accNo<<endl;
        cout<<"Account Holder's Account Type: "<<accType<<endl;
        cout<<"Account Holder's Available Balance: "<<accBal<<endl;
    }
    void modifyAccount(){  //Modifies Account Details
        cout<<"\n---------------------------------------"<<endl;
        cout<<"Enter New Details of"<<accName<<endl;
        cout<<"---------------------------------------"<<endl;
        cout<<"Name: ";
        cin >> accName;
        cout<<"Account Number: ";
        cin >> accNo;
        cout<<"Account Type: ";
        cin >> accType;
        cout<<"Available Balnace: ";
        cin >> accBal;
        cout<<"\n\n     DETAILS UPDATED   "<<endl;
    }
    void depositAmount(int amt){  //Deposit money from Account
        accBal += amt;
        cout<<"\n AMOUNT DEPOSITED SUCESSFULLY"<<endl;
        cout<<"\n UPDATED AMOUNT: "<<returndeposit()<<endl;
    }
    void widrawAmount(int amt){  //Widraw money from Account
        accBal -= amt;
        cout<<"\n AMOUNT WIDRAWED SUCESSFULLY"<<endl;
        cout<<"\n UPDATED AMOUNT: "<<returndeposit()<<endl;
    }
    void report(){  // Shows details in tabular form
        cout<<"---------------------------------------";
        cout<<"\nAccount Holder's Name: "<<accName<<endl;
        cout<<"Account Holder's Account Number: "<<accNo<<endl;
        cout<<"Account Holder's Account Type: "<<accType<<endl;
        cout<<"Account Holder's Available Balance: "<<accBal<<endl;
    }
    int returnaccno(){return accNo;}     //returns Account No.
    int returndeposit(){return accBal;}  //returns Account Balance 
    char returntype(){return *accType;}  //returns Account Type
};

// Defining Functions Beforehand
void intro();               //Shows inroduction page
void write_account();       //Creates Account 
void display_sp(int);       //Displays Account Details
void modify_account(int);   //Modifies Account Details
void delete_account(int);   //Deletes Account Details 
void deposit(int,int);      //Deposit money from Account 
void widraw(int,int);       //Widraw money from Account 
void display_all();         //Displays All Account details

//Main Function
int main(){
    int opt,accno,amt;
    while (true){  //Looping the Whole Code
      intro();     //Showing the Main Menue
      cin>>opt;
      switch(opt){
          case 1:
            write_account();
            break;
          case 2:
            cout<<"Enter Account No. to Display details of: ";
            cin>>accno;
            display_sp(accno);
            break;
          case 3:
            cout<<"Enter Account No. to Modify Details of: ";
            cin>>accno;
            modify_account(accno);
            break;
          case 4:
            cout<<"Enter Account No. to Delete: ";
            cin>>accno;
            delete_account(accno);
            break;
          case 5:
            cout<<"Enter Account No. to deposit: ";
            cin>>accno;
            cout<<"Enter the amount to deposit: ";
            cin>>amt;
            deposit(accno,amt);
            break;
          case 6:
            cout<<"Enter Account No. to Widraw: ";
            cin>>accno;
            cout<<"Enter the amount to Widraw: ";
            cin>>amt;
            widraw(accno,amt);
            break;
          case 7:
            display_all();
            break;
          case 8:
            exit(1);
          default:
            cout<<"Wrong Choice Entered"<<endl;
        }  
    }
    return 0 ;
}    
//Into or Main Menue
void intro(){
    cout<<"\n-------------------------------------------------"<<endl;
    cout<<"|\t\tWELCOME TO MST BANK\t\t|"<<endl;
    cout<<"-------------------------------------------------"<<endl;
    cout<<"1. Create a new Account"<<endl;
    cout<<"2. Display User;s Account Details"<<endl;
    cout<<"3. Modify User's Account details"<<endl;
    cout<<"4. Delete User's Account"<<endl;
    cout<<"5. Deposit money from account"<<endl;
    cout<<"6. Widraw money from account"<<endl;
    cout<<"7. Display all Account's Details"<<endl;
    cout<<"8. EXIT"<<endl;
    cout<<"-------------------------------------------------"<<endl;
    cout<<"ENTER YOUR CHOICE: ";
}

//Write User details to file
void write_account(){
Account user;
ofstream oFile;
oFile.open("user.dat",ios::binary|ios::app);
user.createAccount();
oFile.write(reinterpret_cast<char *> (&user), sizeof(Account));
//oFile.write(sizeof(Account))
oFile.close();
cout<<"\n\nUser record Has Been Created ";
}

//Show user record based on Acc No.
void display_sp(int n){
Account user;
ifstream iFile;
iFile.open("user.dat",ios::binary);
if(!iFile){
  cout<<"File could not be opened... Press any Key to exit";
  cin.get();
  return;
}
bool flag=false;
while(iFile.read(reinterpret_cast<char *> (&user), sizeof(Account))){
  if(user.returnaccno()==n){
    user.showAccount();
    flag=true;
  }
}
iFile.close();
if(flag==false){
  cout<<"\n\nrecord does not exist";
  cin.ignore();
  }
}

// Modify record for specified Account Number
void modify_account(int n){
bool found=false;
Account user;
fstream fl;
fl.open("user.dat",ios::binary|ios::in|ios::out);
if(!fl){
  cout<<"File could not be opened. Press any Key to exit...";
  cin.ignore();
  cin.get();
  return;
}
while(!fl.eof() && found==false){
  fl.read(reinterpret_cast<char *> (&user), sizeof(Account));
  if(user.returnaccno()==n){
    user.showAccount();
    cout<<"\n\Enter new student details:"<<endl;
    user.modifyAccount();
    int pos=(-1)*static_cast<int>(sizeof(user));
    fl.seekp(pos,ios::cur);
    fl.write(reinterpret_cast<char *> (&user), sizeof(Account));
    cout<<"\n\n\t Record Updated";
    found=true;
    }
}
fl.close();
if(found==false)
  cout<<"\n\n Record Not Found ";
  cin.ignore();
  cin.get();
}

// Delete record with particular Account Number
void delete_account(int n){
Account user;
ifstream iFile;
iFile.open("user.dat",ios::binary);
if(!iFile){
  cout<<"File could not be opened... Press any Key to exit...";
  cin.ignore();
  cin.get();
  return;
}
ofstream oFile;
oFile.open("Temp.dat",ios::out);
iFile.seekg(0,ios::beg);
while(iFile.read(reinterpret_cast<char *> (&user), sizeof(Account))){
  if(user.returnaccno()!=n){
    oFile.write(reinterpret_cast<char *> (&user), sizeof(Account));
  }
}
oFile.close();
iFile.close();
remove("user.dat");
rename("Temp.dat","user.dat");
cout<<"\n\n\tRecord Deleted ..";
cin.ignore();
}
// Display all user records
void display_all(){
Account user;
ifstream inFile;
inFile.open("user.dat",ios::binary);
if(!inFile){
  cout<<"File could not be opened !! Press any Key to exit";
  cin.ignore();
  cin.get();
  return;
}
cout<<"\n\n\n\t\tDISPLAYING ALL RECORDS\n\n";
while(inFile.read(reinterpret_cast<char *> (&user), sizeof(Account))){
  user.showAccount();
  cout<<"\n\n====================================\n";
}
inFile.close();
cin.ignore();
}

// Deposit money
void deposit(int n,int amt){
bool found=false;
Account user;
fstream fl;
fl.open("user.dat",ios::binary|ios::in|ios::out);
if(!fl){
  cout<<"File could not be opened. Press any Key to exit...";
  cin.ignore();
  cin.get();
  return;
}
while(!fl.eof() && found==false){
  fl.read(reinterpret_cast<char *> (&user), sizeof(Account));
  if(user.returnaccno()==n){
    user.depositAmount(amt);
    int pos=(-1)*static_cast<int>(sizeof(user));
    fl.seekp(pos,ios::cur);
    fl.write(reinterpret_cast<char *> (&user), sizeof(Account));
    cout<<"\n\n\t Record Updated";
    found=true;
}
}
fl.close();
if(found==false)
  cout<<"\n\n Record Not Found ";
  cin.ignore();
  cin.get();
}

// Widraw money
void widraw(int n,int amt){
bool found=false;
Account user;
fstream fl;
fl.open("user.dat",ios::binary|ios::in|ios::out);
if(!fl){
  cout<<"File could not be opened. Press any Key to exit...";
  cin.ignore();
  cin.get();
  return;
}
while(!fl.eof() && found==false){
  fl.read(reinterpret_cast<char *> (&user), sizeof(Account));
  if(user.returnaccno()==n){
    user.widrawAmount(amt);
    int pos=(-1)*static_cast<int>(sizeof(user));
    fl.seekp(pos,ios::cur);
    fl.write(reinterpret_cast<char *> (&user), sizeof(Account));
    cout<<"\n\n\t Record Updated";
    found=true;
  }
}
fl.close();
if(found==false)
  cout<<"\n\n Record Not Found ";
  cin.ignore();
  cin.get();
}









