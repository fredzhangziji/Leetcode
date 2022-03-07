// Greedy Method
/*
int integerReplacement(long n){
    int res = 0;
    while (n >= 1) {
        if (n == 1) {
            return res;
        }
        if (n % 2 == 0) {
            n /= 2;
        } else {
            if (n == 3) {
                return res + 2;
            }
            if ((n + 1) % 4 == 0) {
                n += 1;
            }
            if ((n - 1) % 4 == 0) {
                n -= 1;
            }
        }
        res += 1;
    }
    return res;
}
*/

// DFS
// we have defined the necessary header files here for this problem.
// If additional header files are needed in your program, please import here.
int Min(int a, int b)
{
    if (a > b) {
        return b;
    } else {
        return a;
    }
}

int Dfs(long n, int res)
{
    if (n == 1) {
        return res;
    }
    if (n % 2 == 0) {
        return Dfs(n / 2, res + 1);
    } else {
        return Min(Dfs(n + 1, res + 1), Dfs(n - 1, res + 1));
    }
}

int integerReplacement(long n)
{
    return Dfs(n, 0);
}
