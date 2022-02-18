/**
 * Note: The returned array must be malloced, assume caller calls free().
 */

// Brute force
/*
int* twoSum(int* nums, int numsSize, int target, int* returnSize){
    
    *returnSize = 2;
    int *res = (int *)malloc(*returnSize * sizeof(int));

    for (int i = 0; i < numsSize; i++) {
        for (int j = i+1; j < numsSize; j++) {
            if (nums[i] + nums[j] == target) {
                res[0] = i;
                res[1] = j;
                return res;
            }
        }
    }
    return res;
}
*/

// Hash table using UTHash
struct NumsDict {
    int num;            // key
    int index;          // value
    UT_hash_handle hh;  // handle of the hashtable, makes the structure hashable
};

int* twoSum(int* nums, int numsSize, int target, int* returnSize)
{
    // initialize pointers
    struct NumsDict *hashtable = NULL; // pointing to the hashtable
                                       // MUST be initialized to NULL
    struct NumsDict *element = NULL;   // pointing to the structure
    struct NumsDict *tmp = NULL;       // for freeing the hashtable
    
    // first iteration (initialize the hashtable)
    for (int i = 0; i < numsSize; i++) {
        HASH_FIND_INT(hashtable, &nums[i], element); // if it doesn't find the num, then element will be null
        if (!element) {
            element = (struct NumsDict*)malloc(sizeof(struct NumsDict));
            element->num = nums[i];
            element->index = i;
            HASH_ADD_INT(hashtable, num, element);  // (hashtable pointer, key name, struct pointer)
        }
    }
    
    // iterate the hashtable for debugging purpose
    /*
    HASH_ITER(hh, hashtable, element, tmp) {
        printf("num: %d; index: %d\n", element->num, element->index);
    }
    */
    
    // second iteration (find target)
    // note: 3 + 3 = 6, but 3 is unique, so we have to check this.
    int num2 = 0;
    *returnSize = 2;
    int *res = (int*)malloc(sizeof(int) * (*returnSize)); 
    for (int i = 0; i < numsSize; i++) {
        num2 = target - nums[i];
        HASH_FIND_INT(hashtable, &num2, element);
        if (element) {
            if (element->index == i) {
                continue;
            } else {
                res[0] = i;
                res[1] = element->index;
                return res; 
            }
        }
    }
    return res;
}
