#include <stdio.h>

int main()
{
    int n=5, total = 0, i, j, small, temp, procs[100], k, waiting[10], finish[10];
    float tavg = 0.0, wavg = 0.0;
    int ari[5]={0,2,3,4,5};
    int bur[5]={5,2,7,4,5};
    
    for (i = 0; i < n; i++)
    {
        waiting[i] = 0;
        total += bur[i];
    }
    for (i = 0; i < n; i++)
    {
        for (j = i + 1; j < n; j++)
        {
            if (ari[i] > ari[j])
            {
                temp = ari[i];
                ari[i] = ari[j];
                ari[j] = temp;
                temp = bur[i];
                bur[i] = bur[j];
                bur[j] = temp;
            }
        }
    }
    for (i = 0; i < total; i++)
    {
        small = 3200;
        for (j = 0; j < n; j++)
        {
            if ((bur[j] != 0) && (ari[j] <= i) && (bur[j] < small))
            {
                small = bur[j];
                k = j;
            }
        }
        bur[k]--;
        procs[i] = k;
    }
    k = 0;
    for (i = 0; i < total; i++)
    {
        for (j = 0; j < n; j++)
        {
        if (procs[i] == j)
            {
                finish[j] = i;
                waiting[j]++;
            }
        }
    }
    printf("Process  Finish time  Turnaround time  Waiting time\n");
    for (i = 0; i < n; i++)
    {
        printf("%d\t\t%d\t\t%d\t\t%d\n", i + 1, finish[i] + 1, (finish[i] - ari[i]) + 1, (((finish[i] + 1) - waiting[i]) - ari[i]));
        wavg = wavg + (((finish[i] + 1) - waiting[i]) - ari[i]);
        tavg = tavg + ((finish[i] - ari[i]) + 1);
    }
    printf("\n Average Wating Time: %f\n Average Turnaround Time: %f\n", (wavg / n), (tavg / n));
    return 0;
}