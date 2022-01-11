// can't pass if in O(n^2); have to do it in O(n)

// Kadane's Algorithm

#define max(a, b) ((a) > (b) ? (a) : (b))

int maxSubArray(int* nums, int numsSize){
    int res = INT_MIN;
    int cSum = 0;
    
    for (int i = 0; i < numsSize; i++) {
        // if the new number is not worth keeping, then we restart counting
        cSum = max(cSum + nums[i], nums[i]); 
        res = max(cSum, res);
    }
    return res;
}
