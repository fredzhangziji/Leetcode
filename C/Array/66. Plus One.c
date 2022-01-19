

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* plusOne(int* digits, int digitsSize, int* returnSize){
    digits[digitsSize-1] += 1;
    for (int i = digitsSize-1; i >= 1; i--) {
        if (digits[i] == 10) {
            digits[i] = 0;
            digits[i-1] += 1;
        } else {
            break;
        }
    }
    if (digits[0] != 10) {
        *returnSize = digitsSize;
        int *res = malloc(*returnSize * sizeof(int));
        for (int i = 0; i < digitsSize; i++) {
            res[i] = digits[i];
        }
        return res;
    } else {
        *returnSize = digitsSize + 1;
        int *res = malloc(*returnSize * sizeof(int));
        res[0] = 1;
        res[1] = 0;
        for (int i = 2; i < *returnSize; i++) {
            res[i] = digits[i-1];
        }
        return res;
    }
}
