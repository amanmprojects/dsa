
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
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        ListNode* head = nullptr, *curr;
        head = new ListNode((l1->val + l2->val) % 10, nullptr);
        curr = head;
        int carry = (l1->val+l2->val)/10;
        l1 = l1->next;
        l2 = l2->next;

        while(l1 && l2){
            curr->next = new ListNode((l1->val + l2->val + carry) % 10, nullptr);
            carry = (l1->val + l2->val + carry) / 10;
            curr = curr->next;
            l1 = l1->next;
            l2 = l2->next;
        }
        while(l1) {
            curr->next = new ListNode((l1->val+carry)%10, nullptr);
            carry = (l1->val+carry)/10;
            curr = curr->next;
            l1 = l1->next;
        }
        while(l2) {
            curr->next = new ListNode((l2->val+carry)%10, nullptr);
            carry = (l2->val+carry)/10;
            curr = curr->next;
            l2 = l2->next;
        }
        
        if (carry) {
            curr->next = new ListNode(carry, nullptr);
        }

        return head;
    }
};