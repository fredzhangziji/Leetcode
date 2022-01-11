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
    helper(root->left, res, i);
    helper(root->right, res, i);
    res[*i] = root->val;
    (*i)++;
}

int* postorderTraversal(struct TreeNode* root, int* returnSize){
    int *res = (int*)malloc(100 * sizeof(int));
    *returnSize = 0;
    helper(root, res, returnSize);
    return res;
}
