bool isPalindrome(int x){
    long result;
    int i;
    int y;

    y = x;
    if (x < 0)
        return (false);
    else if (x >= 0 && x <= 9)
        return (true);
    result = 0;
    while (x != 0)
    {
        result *= 10;
        result += (x % 10);
        x /= 10;
    }
    return (result == y ? true : false);
}