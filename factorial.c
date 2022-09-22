// c code to print factorial of a number.
#include<stdio.h>

int fact(int num){
  for(int i = num-1;i>=1;i--){
    num = num*i;
  }
  printf("%d \n",num);
  return 0;
}

int main(){
  int num;
  printf("Enter the number you want to get factorial of: ");
  scanf("%d",&num);
  printf("Factorial of %d = ",num);
  fact(num);
  return 0;
}
