#include <math.h>

using namespace std;
// Definition for a binary tree node.
struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};


class Solution {
public:
    int diameterOfBinaryTree(TreeNode* root) {
        if(root == nullptr) return 0;
        return max(max(getHeight(root->left)+getHeight(root->right), diameterOfBinaryTree(root->left)),  diameterOfBinaryTree(root->right));
    }
private: 
    int getHeight(TreeNode* t){
    if (t == nullptr) return 0;

    return max(1 + getHeight(t->left), 1 + getHeight(t->right));
    }
};
