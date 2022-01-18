uint32_t reverseBits(uint32_t n) {
    uint32_t res = 0;
    int cnt = 32;
    while (cnt > 0) {
        res <<= 1;
        res += n & 1; // res += n % 2;
        n >>= 1;
        cnt--;
    }
    return res;
}
