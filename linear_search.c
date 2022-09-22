#include<stdio.h>
//using namespace std;

void get_data(int len,int arr[]){
  for (int i=0;i<len;i++){
    printf("Enter the value of element %d :",i);
    scanf("%d",&arr[i]);
  }}

void show_data(int len,int arr[]){
  for(int i=0;i<len;i++){
    printf("%d ",arr[i]);
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
  printf("Enter the size of array: ");
  scanf("%d",&len);
  int arr[len];
  printf("\n");
  get_data(len,arr);
  printf("\nThe members of the array are:\n");
  printf("------------------------------------------------------\n");
  show_data(len,arr);
  printf("\n------------------------------------------------------\n\n");
  printf("Enter the number u want to search in array :");
  scanf("%d",&num);
  if (look(len,num,arr) !=  -1){
    printf("Element %d found at %d \n.",num,look(len,num,arr));
  }
  else{
    printf("Element %d not found \n",num); 
  }
  return 0;
}
