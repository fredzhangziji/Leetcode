#include <stdbool.h>

bool isValid(char * s){
    char *stack1[strlen(s)];
    int top = 0;

    for (int i = 0; i < strlen(s); i++) {
        if (s[i] == '(') {
            stack1[top] = s[i];
            top++;
        }
        else if (s[i] == '[') {
            stack1[top] = s[i];
            top++;
        }
        else if (s[i] == '{') {
            stack1[top] = s[i];
            top++;
        }
        else if (s[i] == ')') {
            if (top == 0) {
                return false;
            }
            if (stack1[top-1] == '(') {
                top--;
            } else {
                return false;
            }
        }
        else if (s[i] == ']') {
            if (top == 0) {
                return false;
            }
            if (stack1[top-1] == '[') {
                top--;
            } else {
                return false;
            }
        }
        else if (s[i] == '}') {
            if (top == 0) {
                return false;
            }
            if (stack1[top-1] == '{') {
                top--;
            } else {
                return false;
            }
        }
    }
    if (top == 0) {
        return true;
    } else {
        return false;
    }
}