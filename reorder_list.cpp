
#include <vector>

using namespace std;
// Definition for singly-linked list.
struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};


class Solution {
public:
    void reorderList(ListNode* head) {
        if (head == nullptr || head->next == nullptr) return;

        vector<ListNode*> arr;
        ListNode* headCopy = head;

        while(headCopy != nullptr){
            arr.push_back(headCopy);
            headCopy=headCopy->next;
        }
        int l = 0;
        int r = arr.size() - 1;
        
        while(l < r){
            arr[l]->next = arr[r];
            l++;

            if (l == r) break;

            arr[r]->next = arr[l];
            r--;
        }

        arr[l]->next = nullptr;
    }
    
};
