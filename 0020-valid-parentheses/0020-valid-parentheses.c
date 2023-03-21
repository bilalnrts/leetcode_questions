#include <stdlib.h>
#include <string.h>

bool isValid(char * s){
    char *stack;
    int top;

    top = -1;
    stack = malloc(strlen(s));
    while(*s!='\0')
    {
        if(*s == '(' || *s == '[' || *s == '{' )
            stack[++top]=*s;
        else if(*s==')')
        {
            if(top == -1 || stack[top] != '(')
                return (false);
            else
                top--;
        }
         else if(*s == ']')
         {
            if(top == -1 || stack[top] != '[')
                return (false);
            else
                top--;
        }
         else if(*s == '}')
         {
            if(top == -1 || stack[top] != '{')
                return (false);
            else
                top--;
         }

        s++;
    }
    return (top == -1 ? true : false);
}