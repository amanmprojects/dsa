
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
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        if( head->next == nullptr) return nullptr;
        // Finding length
        ListNode* head2 = head;
        int count = 0;
        while(head2 != nullptr) {
            count++; 
            head2 = head2->next;
        }
        head2 = head;
        int target = count - n;

        if(target == 0) {
            head = head->next;
            return head;
        }

        int i = 0;
        
        while(i<target-1){
            head2 = head2->next;
            i++;
        }

        head2->next = head2->next->next;

        return head;
    }
};
