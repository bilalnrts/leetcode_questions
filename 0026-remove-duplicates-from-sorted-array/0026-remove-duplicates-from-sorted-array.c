#include <stdlib.h>
#include <stdio.h>
#include <unistd.h>
#include <string.h>

int is_unique(int n, int *arr, int size)
{
    int i;
    
    i = 0;
    while (i < size)
    {
        if (arr[i] == n)
            return (0);
        i++;
    }
    return (1);
}

int removeDuplicates(int* nums, int numsSize)
{
    int *arr;
    int i,j;
    
    i = 0;
    j = 0;
    arr = malloc(sizeof(int) * numsSize);
    if (!arr)
        return (0);
    while (i < numsSize)
    {
        if (is_unique(nums[i], arr, j))
        {
            arr[j] = nums[i];
            j++;
        }
        i++;
    }
    for (i = 0; i < j; i++)
        nums[i] = arr[i];
    return (j);
}