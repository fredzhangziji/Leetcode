#define MAX_ROW 100
#define MAX_COL 100

int matrix[MAX_ROW][MAX_COL];

int Max(int a, int b)
{
    if (a > b) {
        return a;
    } else {
        return b;
    }
}

int Dfs(int i, int j, int n, int m, int sum)
{
    // edge case
    if (i < 0 || j < 0 || (i + 1) > n || (j + 1) > m) {
        return 0;
    }
    
    // base case （dfs的递归出口）
    if (i == n - 1 && j == m - 1) {
        return sum;
    }

    // going down or going right
    return Max(Dfs(i + 1, j, n, m, sum + matrix[i + 1][j]), \
               Dfs(i, j + 1, n, m, sum + matrix[i][j + 1]));
}


int main()
{
    // read in the col and row numbers
    int n;
    int m;
    scanf("%d%d", &n, &m);
    
    // fill in the matrix
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            scanf("%d", &matrix[i][j]);
        }
    }
    
    // call dfs
    int res;
    res = Dfs(0, 0, n, m, matrix[0][0]);
    printf("%d", res);
    
    return 0;
}
