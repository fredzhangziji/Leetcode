// binary search O(log n)
int searchInsert(int* nums, int numsSize, int target) {
    int mid;
    int start = 0;
    int end = numsSize - 1;
    
    while (start <= end) {
        mid = (end + start) / 2;
        if (nums[mid] < target) {
            start = mid + 1;
        } else if (nums[mid] > target) {
            end = mid - 1;
        } else {
            return mid;
        }
    }
    return start;
}

// brute force O(n)
// int searchInsert(int* nums, int numsSize, int target){
//     int res;
//     int pointer = 0;
    
//     while (pointer < numsSize) {
//         if (nums[pointer] < target) {
//             pointer++;
//         } else if (nums[pointer] == target) {
//             return pointer;
//         } else {    // nums[pointer] > target
//             return pointer;
//         }
//     }
//     return pointer;
// }
