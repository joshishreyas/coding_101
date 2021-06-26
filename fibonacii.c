#include<stdio.h>
int main(void){
	int sum=1;
	int a=0,b=1,n;
	
	printf("Enter the nth term: ");
	scanf("%d",&n);
	printf("Fibonacii series till n:\n ");
	while (sum<=n){
		printf("%d\t",sum);
		a=b;
		b=sum;
		sum=a+b;
	}
	//return 0;
}
