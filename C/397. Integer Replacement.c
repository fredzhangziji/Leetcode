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
