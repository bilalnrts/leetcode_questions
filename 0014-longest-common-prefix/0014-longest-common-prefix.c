char * longestCommonPrefix(char ** strs, int strsSize){
    int i;
    int j;
    
    i = 0;

    while (1)
    {
        if (!strs[0][i])
            return (strs[0]);
        j = 1;
        while (j < strsSize)
        {
            if (strs[j][i] != strs[0][i])
            {
                strs[0][i] = '\0';
                return (strs[0]);
            }
            j++;
        }
        i++;
    }
}