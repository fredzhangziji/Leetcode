

int singleNumber(int* nums, int numsSize){
    // 0 ^ a = a
    // 一个数字异或0还是等于这个数字
    // (a ^ b) ^ b = a
    // 一个数字异或两次另一个数字，结果还是这个第一个数字。
    
    int res = 0;
    numsSize--;
    while (numsSize >= 0) {
        res ^= nums[numsSize];
        numsSize--;
    }
    return res;
}
