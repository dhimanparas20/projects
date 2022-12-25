#include <iostream>
using namespace std;

void sort(int array[], int size) {  //for sorting the elements of array
  for (int i = 0; i < size; i++) {
    for (int j = 0; j < size; j++) {
      if (array[j] > array[j + 1]) {
        int temp = array[j];
        array[j] = array[j + 1];
        array[j + 1] = temp;
      }
    }
  }
}

int look(int arr[],int low,int high,int x){  // recursive function to look for elements of array
    if (high>=low){
        int mid = low + (high-low)/2;
        if (x==arr[mid]){
            return mid;
        }
        if (x<arr[mid]){
            return look(arr,low,mid-1,x);
        }
        return look(arr,mid+1,high,x);
    }
    return -1;
}

int main()
{
    int arr[5]={56,234,455,57,84},i=0;
    int size = sizeof(arr)/sizeof(arr[0]);
    sort(arr,size);
    // 56 57 84 234 455
    for (i;i<size;i++){   //displaying sorted elements
        cout<<arr[i]<<" ";
    }
    cout<<"\n";
    cout<<look(arr,0,4,84);
    
    return 0;
}
