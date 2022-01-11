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
int res[100];
int i = -1; // index for res

void helper(struct TreeNode* root) {
    if (root == NULL) {
        return;
    }
    
    helper(root->left);
    i++;
    res[i] = root->val;
    helper(root->right);
}


int* inorderTraversal(struct TreeNode* root, int* returnSize){
    // edge case
    if (root == NULL) {
        *returnSize = 0;
        return res;
    }
    
    helper(root);
    *returnSize = i + 1;    // return size = the final index + 1
    i = -1;                 // reset the extern variable
    return res;

}

