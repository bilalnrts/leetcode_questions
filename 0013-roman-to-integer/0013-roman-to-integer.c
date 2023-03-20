int romanToInt(char * s){
    int result;
    int i;

    if (!s)
        return (0);
    result = 0;
    i = 0;
    while (s[i])
    {
        if (s[i] == 'M')
            result += 1000;
        else if (s[i] == 'D')
            result += 500;
        else if (s[i] == 'C' && (s[i + 1] != 'M' && s[i + 1] != 'D'))
            result += 100;
        else if (s[i] == 'C' && (s[i + 1] == 'M' || s[i + 1] == 'D'))
        {
            if (s[i + 1] == 'D')
                result += 400;
            else
                result += 900;
            i++;
        }
        else if (s[i] == 'L')
            result += 50;
        else if (s[i] == 'X' && (s[i + 1] != 'L' && s[i + 1] != 'C'))
            result += 10;
        else if (s[i] == 'X' && (s[i + 1] == 'L' || s[i + 1] == 'C'))
        {
            if (s[i + 1] == 'L')
                result += 40;
            else
                result += 90;
            i++;
        }
        else if (s[i] == 'V')
            result += 5;
        else if (s[i] == 'I' && (s[i + 1] != 'V' && s[i + 1] != 'X'))
            result += 1;
        else if (s[i] == 'I' && (s[i + 1] == 'V' || s[i + 1] == 'X'))
        {
            if (s[i + 1] == 'V')
                result += 4;
            else
                result += 9;
            i++;
        }
        i++;
    }
    return (result);    
}