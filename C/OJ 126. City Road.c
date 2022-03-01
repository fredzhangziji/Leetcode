int p[1001];

int Find(int n)
{
    if (n == p[n]) {
        return n;
    } else {
        p[n] = Find(p[n]);
        return p[n];
    }
}

void Join(int a, int b, int *n)
{
    int aa = Find(a);
    int bb = Find(b);
    if (aa == bb) {
        return; 
    } else {
        // if there is a bridge
        // update the 并查集 and update the answer
        p[aa] = bb;
        
        // n here means the no. disjointed islands 
        *n = *n - 1;
    }
}

int main()
{
    // read in the no. of islands and no. of bridges 
    int n;
    int m;
    scanf("%d %d", &n, &m);
    
    // initialize the 并查集
    for (int i = 1; i <= n; i++) {
        p[i] = i;
    }
    
    // read in the bridges and update the 并查集
    int a;
    int b;
    while (m > 0) {
        scanf("%d %d", &a, &b);
        Join(a, b, &n);
        m--;
    }
    
    // n here means the no. disjointed islands 
    printf("%d", n - 1);
    
    return 0;
}
