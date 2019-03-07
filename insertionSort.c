#include<stdio.h>
void main()
{
	int n,i,a[100];
	printf("\nEnter number of elements:");
	scanf("%d",&n);
	printf("\nEnter the elements:");
	for(i=0;i<n;i++)
	{
		scanf("%d",&a[i]);
	}
	printf("\nThe Elements before sorting are: ");
	for(i=0;i<n;i++)
	{
		printf("%d ",a[i]);
	}
	
	insertionSort(a,n);
	
	return 0;
}

void insertionSort(int a[],int n)
{
	int i,key,j;
	for(i=1;i<n;i++)
	{
		key = a[i];
		j = i-1;
		while(j>=0 && a[j]>key)
		{
			a[j+1]=a[j];
			j = j-1;
		}
		a[j+1]=key;
	}
	printf("\nThe Elements after sorting are: ");
	for(i=0;i<n;i++)
	{
		printf("%d ",a[i]);
	}
		
}
