/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */


/**
 * Note: The returned array must be malloced, assume caller calls free().
 */

// 不用全局变量
void helper(struct TreeNode* root, int* res, int* i) {
    if (root == NULL) {
        return;
    }
    helper(root->left, res, i);
    res[*i] = root->val;
    (*i)++;
    helper(root->right, res, i);
}


int* inorderTraversal(struct TreeNode* root, int* returnSize){
    int *res = (int*)malloc(100 * sizeof(int));
    *returnSize = 0;
    helper(root, res, returnSize);
    return res;
}

// 用全局变量
// int res[100];
// int i = -1; // index for res

// void helper(struct TreeNode* root) {
//     if (root == NULL) {
//         return;
//     }
//     helper(root->left);
//     i++;
//     res[i] = root->val;
//     helper(root->right);
// }


// int* inorderTraversal(struct TreeNode* root, int* returnSize){
//     // edge case
//     if (root == NULL) {
//         *returnSize = 0;
//         return res;
//     }
    
//     helper(root);
//     *returnSize = i + 1;    // return size = the final index + 1
//     i = -1;                 // reset the extern variable
//     return res;
// }
