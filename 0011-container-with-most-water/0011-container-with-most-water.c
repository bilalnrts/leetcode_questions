int ft_min(int first, int sec)
{
    return (first < sec ? first : sec);
}

int maxArea(int* height, int heightSize){
    int start;
    int end;
    int highest;
    int current;
    
    start = 0;
    highest = 0;
    end = heightSize - 1;
    while (start < end)
    {
        current = ft_min(height[start], height[end]) * (end - start);
        if (current > highest)
            highest = current;
        if (height[start] < height[end])
            start++;
        else
            end--;
    }
    return (highest);
}