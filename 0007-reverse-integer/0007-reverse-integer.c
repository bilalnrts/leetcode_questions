int reverse(int x){
    long result;
    int sign;
    
    result = 0;
    sign = 1;
    if (x < 0 && x != -2147483648)
    {
        sign = -1;
        x *= -1;
    }
    while (x)
    {
        result = (result * 10) + (x % 10);
        if (result > 2147483647 || result < -2147483648)
            return (0);
        x /= 10;
    }
    return (sign * result);
}