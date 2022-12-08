#include <stdio.h>

int main() {
	int WT[4], TAT[4], FT[4];
	int process[4] = {1, 2, 3, 4};
	int burst[4]= {53, 17, 68, 24};
	int temp[4];  
	int q = 20, time = 0, flag = 0, n=4;

	int i;
	for (i = 0; i < n; i++) 
	{
		temp[i] = burst[i];
	}

	for(;;) 
	{
	
		if (flag == 1) {
				break;
		}
		
		flag = 1;
		int i;
		for (i = 0; i < n; i++) 
		{
			if (temp[i] != 0) {
			
				if (temp[i] > q) 
				{
					time += q;
					temp[i] -= q;
				}
				else 
				{
					time += temp[i];
					WT[i] = time - burst[i];
					temp[i] = 0;
				}
				flag = 0;
			}	
		}
	}
	
	printf("Process\t Finishing Time\t Wainting Time\t Turnaround Time\n");
	for (int i = 0; i < n; i++) {
		TAT[i] = burst[i] + WT[i];
		FT[i] = TAT[i] - 0; 
		printf("%d\t\t%d\t\t%d\t\t%d\n", i+1, FT[i], WT[i], TAT[i]);
	}
}