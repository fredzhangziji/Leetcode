#include <limits.h>
#define LARGENUM 1000000

int Dfs(int a, int b)
{
    if (b == 1) {
        return a - 1;
    }
    
    if (a % b != 0) {
        return Dfs(b, a%b) + a/b; 
    }
    
    // a % b == 0, will never reach (1, 1)
    return LARGENUM;
}

int main()
{
    int n;
    int count;
    int min;
    
    while (scanf("%d", &n) != EOF) {
        min = INT_MAX;
        for (int i = 1; i <= n / 2 + 1; i++) {
            count = Dfs(n, i);
            min = min < count ? min : count;
        }
        printf("%d\n", min);
    }
    return 0;
}
