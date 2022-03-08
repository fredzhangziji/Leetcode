int res;

void Dfs(int start, int score, int n, int s)
{
    // base case
    if (start == n) {
        if (score == s) {
            res++;
        }
        return;
    }
    
    // correct and wrong cases
    Dfs(start + 1, score * 2, n, s);
    Dfs(start + 1, score - start - 1, n, s);
    
}

int main()
{
    int n;
    int s;
    scanf("%d%d", &n, &s);
    
    // correct and wrong cases
    Dfs(1, 10 * 2, n, s);
    Dfs(1, 10 - 1, n, s);
    printf("%d", res);
    
    return 0;
}
