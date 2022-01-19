

int removeDuplicates(int* nums, int numsSize){
    // edge case
    if (numsSize <= 1) {
        return numsSize;
    }
    
    int k = 0;
    for (int i = 1; i < numsSize; i++) {
        if (nums[i-1] < nums[i]) {  // which means this pair is valid
            k++;                    // means we can increment the valid length by 1
            nums[k] = nums[i];      // modify the array in-place
        }
    }

    return k+1;
}
