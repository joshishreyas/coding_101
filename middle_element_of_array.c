#include<stdio.h>
int main(void){
	int arr[20];
	int n,i;
	printf("Enter the size of array: ");
	scanf("%d",&n);
	printf("\nEnter the elements of array: ");
	for(i=0;i<n;i++){
		scanf("%d",&arr[i]);
	}
	
	int len = sizeof(arr)/sizeof(arr[0]);
	int mid = len/2;
	printf("Middle element of array is %d",arr[mid]); 
	
}
