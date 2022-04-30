#include<stdio.h>

void binary(int num,int k)
{
	int pos,i;
	for(i=0;i<k;i++)
	{
		for(pos=num-1;pos>=0;pos--)
		{
			printf("%d",i>>pos&1);	
		}
		printf("\n");
	}
}
int main()
{
	int num,i,j,m;
	printf("Enter integer..\n");
	scanf("%d",&num);
	for(i=0,m=1;i<num;i++)
	{
		m=2*m;
	}
	printf("%d \n",m);
	binary(num,m);
}
