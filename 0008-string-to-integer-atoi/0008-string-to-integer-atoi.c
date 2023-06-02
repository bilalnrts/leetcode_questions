int myAtoi(char * s)
{
    long result;
    int sign;
    int i;

    i = 0;
    sign = 1;
    result = 0;
    while (s[i] == ' ' || (s[i] <= 13 && s[i] >= 9))
        i++;
    if (s[i] == '+' || s[i] == '-')
    {
        if (s[i] == '-')
            sign = -1;
        i++;
    }
    while (s[i] >= '0' && s[i] <= '9')
    {
        result = (result * 10) + (s[i] - 48);
        if (result > 2147483647)
        {
            if (sign == 1)
                return (2147483647);
            return (-2147483648);
        }
        i++;
    }
    return (result * sign);
}