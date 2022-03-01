#define MAXN 100001
#define INF (1e9+7)

int dp[MAXN];       // dp table
int A[MAXN];        // coin cost array (input)
int pre[MAXN];      // previous hop location
int len[MAXN];      // path length (for dictionary order)
int b;              // max number of hop (input)
int arrayLength;    // size of the array

void Print(int n)
{
    // if the destination is -1, that means it has no valid path
    if(dp[n] == INF) {
        printf("-1\n");
        return;
    }

    // base case
    if (n == 0) {
        return;
    }

    // get the previous hop
    Print(pre[n]);
    printf("%d%c", n, ((n==arrayLength) ? '\n' : ' '));
}

int main()
{
    // read in b (max number of hops)
    scanf("%d", &b);

    // read in coin cost into the array A, and update the array length
    int coin;
    while (scanf("%d", &coin) != EOF) {
        arrayLength++;
        A[arrayLength] = coin;
    }

    // initialize the dp as INF
    for (int i = 1; i <= arrayLength; i++) {
        dp[i] = INF;
    }

    // fill in the starting values
    dp[1] = (A[1] == -1) ? INF : A[1];
    pre[1] = 0;
    len[1] = 1;

    // dp
    for (int i = 1; i <= arrayLength; i++) {
        if(dp[i] == INF) {
            continue;
        }
        for(int j = 1; j <= b; j++){
            // the hop is invalid
            if(i + j > arrayLength || A[i + j] == -1) {
                continue;
            }

            // 1. if this +j hop has less coin cost
            // 2. if the +j hop has the same coin cost but less length
            if (dp[i + j] > dp[i] + A[i + j] || (dp[i + j] == dp[i] + A[i + j] && len[i + j] < len[i] + 1)) {
                dp[i + j] = dp[i] + A[i + j]; // update cost
                pre[i + j] = i;               // update path
                len[i + j] = len[i] + 1;      // update path ength
            }
        }
    }

    Print(arrayLength);
    return 0;
}
