/* Hashtable method by UTHash */
struct NumsDict {
    int num;            // key
    int count;          // value
    UT_hash_handle hh;   // handle of hashtable, makes the structrue hashable
};

bool containsDuplicate(int* nums, int numsSize)
{
    /* initialize pointers */
    struct NumsDict *hashtable = NULL;  // pointing to the hashtable
                                        // MUST be initialized to NULL!
    struct NumsDict *element = NULL;    // pointting to the structure
    struct NumsDict *tmp = NULL;        // for freeing
    
    /* iterate through the list */
    for (int i = 0; i < numsSize; i++) {
        HASH_FIND_INT(hashtable, &nums[i], element);
        if (element) {          // if it exists
            // free the memory
            HASH_ITER(hh, hashtable, element, tmp) {
                free(element);
            }
            return true;
        } else {                // if it doesn't exist
            element = (struct NumsDict*)malloc(sizeof(struct NumsDict));
            element->num = nums[i];
            element->count = 1;
            HASH_ADD_INT(hashtable, num, element);
        }
    }
    return false;
}


/* Sorting method by qsort */
// int CmpFunc(const void *a, const void *b)
// {
//     return (*(int*)a - *(int*)b);
// }

// bool containsDuplicate(int* nums, int numsSize)
// {
//     // First, sort the list
//     qsort(nums, numsSize, sizeof(int), CmpFunc);
    
//     // Then, compare consecutive numbers
//     for (int i = 0; i < numsSize - 1; i++) {
//         if (nums[i] == nums[i + 1]) {
//             return true;
//         }
//     }
//     return false;
// }
