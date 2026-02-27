#include <vector>
#include <stack>
#include <iostream>

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
    bool isSameTree(TreeNode* a, TreeNode* b) {
        if(!a && !b) return true;
        else if(a && !b || !a && b) return false;

        if(!(a->val == b->val)) return false;
        return (isSameTree(a->left, b->left) && isSameTree(a->right, b->right));
    } 
    bool isSubtree(TreeNode* root, TreeNode* subRoot) {
        // DFS
        stack<TreeNode*> s;
        s.push(root);

        while(!s.empty()){
            TreeNode* curr = s.top();
            cout<<"current value: "<<curr->val<<"\n";
            if(curr->val == subRoot->val && isSameTree(curr, subRoot)) {
                return true;
            }
            else {
                s.pop();
                if(curr->right) s.push(curr->right);
                if(curr->left) s.push(curr->left);
            }

        }
        return false;
    }
};
