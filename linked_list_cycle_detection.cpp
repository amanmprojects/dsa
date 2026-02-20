#include <unordered_set>

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
    bool hasCycle(ListNode* head) {
        unordered_set<ListNode*> s;

        ListNode *curr = head;

        while(curr != nullptr){
            if(s.count(curr)){
                return true;
            }
            s.insert(curr);
            curr = curr->next;
        }

        return false;
    }
};