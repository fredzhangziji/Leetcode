/*
This is a recursive function.
index:         current node's value
count:         the order/rank of the ball when it passes the current node
               this is used for deciding if it's going left or right
currentDepth:  current node's depth 
maxDepth:      the depth of the tree - d
*/
void BallDown(int index, int count, int currentDepth, int maxDepth)
{
    // base case
    if (currentDepth == maxDepth) {
        printf("%d\n", index);
        return;
    }
    
    // recursive call
    if (count % 2 == 0) {    // going right
        BallDown(index * 2 + 1, count / 2, currentDepth + 1, maxDepth);
    }
    
    if (count % 2 == 1) {    // going left
        BallDown(index * 2, (count + 1) / 2, currentDepth + 1, maxDepth);
    }
    
    // return;
}

int main()
{
    // please define the C input here. For example: int n; scanf("%d",&n);
    // please finish the function body here. 
    // please define the C output here. For example: printf("%d\n",a);  
    int n;
    int d;
    while (scanf("%d %d", &d, &n) != EOF) {
        BallDown(1, n, 1, d);
    }
    
    return 0;
}
