int main()
{
    char path[1000][20] = {{0}}; // regard path as a stack
    strcpy(path[1], "Users");
    strcpy(path[2], "hp");
    printf("C:\\Users\\hp>\n");
    int top = 2; // pointing to the current stack top
    
    int n;
    scanf("%d", &n);
    char cd[20];
    char inputCmd[20];
    
    while (n > 0) {
        scanf("%s%s", cd, inputCmd);
        // if it's a valid path, we push it into the stack and move the stack top
        if (strcmp(inputCmd, "..") != 0) {
            top++;
            strcpy(path[top], inputCmd);
        // if it's a .. cmd, we move the stack top back by 1
        // also we need to check if there is any space for the top to move back
        } else {
            if (top > 0) {
                top--;
            }
        }
        
        // print out the path after every cmd
        printf("C:\\");
        for (int i = 1; i < top; i++) {
            printf("%s\\", path[i]);
        }
        printf("%s", path[top]);
        printf(">\n");
        n--;
    }

    return 0;
}
