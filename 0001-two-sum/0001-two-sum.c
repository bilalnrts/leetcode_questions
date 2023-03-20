/**
 * Note: The returned array must be malloced, assume caller calls free().
 */

int* twoSum(int* nums, int numsSize, int target, int* returnSize){
    int i = 0;
    int j;
    int *mylist = malloc(2 * sizeof(int));
    while (i < numsSize)
    {
        j = i + 1;
        while (j < numsSize)
        {
            if (nums[i] + nums[j] == target)
            {
                *returnSize = 2;
                mylist[0] = i;
                mylist[1] = j;
                return (mylist);
            }
            j++;
        }
        i++;
    }
    return ;
}