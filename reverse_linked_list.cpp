

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
    ListNode* reverseList(ListNode* head) {
        ListNode* curr, *prev = nullptr, *next;
        
        while(head != nullptr){
            curr = head;
            next = curr->next;
            curr->next = prev;
            prev = curr;
            head = next;
        }
        return prev;
    }
};
