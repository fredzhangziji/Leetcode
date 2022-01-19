#define LOOPSIZE 32

int hammingWeight(uint32_t n) {
    int cnt = 0;
    for (int i = 0; i < LOOPSIZE; i++) {
        if (n & 1 == 1) {
            cnt++;
        }
        n >>= 1;
    }   
    return cnt;
}
