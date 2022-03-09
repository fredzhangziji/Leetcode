int path[16];
int visited[16];
int prime[30];

void isPrime(int n)
{
    for (int i = 0; i < n; i++) {
        if (i == 0) {
            prime[i] = 0;
        } else if (i == 1) {
            prime[i] = 1;
        } else {
            int primeFlag = 1;
            for (int j = 2; j <= sqrt(i); j++) {
                if (i != j && i % j == 0) {
                    primeFlag = 0;
                }
            }
            if (primeFlag == 1) {
                prime[i] = 1;
            } else {
                prime[i] = 0;
            }
        }
    }
}

void Dfs(int start, int n)
{
    if (start == n) {
        if (!(prime[path[0] + path[n - 1]])) {
            return;
        } else {
            int i;
            for (i = 0; i < n - 1; i++) {
                printf("%d ", path[i]);
            }
            printf("%d\n", path[i]);
            return;
        }
    }
    for (int i = 2; i <= n; i++) {
        if (visited[i] == 0) { 
            if (prime[path[start - 1] + i]) {
                path[start] = i;
                visited[i] = 1;
                Dfs(start + 1, n);
                visited[i] = 0;    // IMPORTANT!!
            }
        }
    }
}

int main()
{
    // fill in the isPrime list
    isPrime(30);
    
    // the first ring is always 1
    visited[1] = 1;
    path[0] = 1;
    
    int n;
    int count = 1;
    while (scanf("%d", &n) != EOF) {
        printf("Case %d:\n", count);
        Dfs(1, n);
        count++;
        printf("\n");
    }
    return 0;
}
