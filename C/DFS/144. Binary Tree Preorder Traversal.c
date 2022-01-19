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
void helper(struct TreeNode* root, int *res, int *i) {
    if (root == NULL) {
        return;
    }
    
    res[*i] = root->val;
    (*i)++;
    helper(root->left, res, i);
    helper(root->right, res, i);
}

int* preorderTraversal(struct TreeNode* root, int* returnSize){
    *returnSize = 0;
    int *res = (int*)malloc(100 * sizeof(int));
    helper(root, res, returnSize);
    return res;
}
