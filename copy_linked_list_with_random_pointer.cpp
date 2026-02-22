#include <unordered_map>

using namespace std;

// Definition for a Node.
class Node {
public:
    int val;
    Node* next;
    Node* random;
    
    Node(int _val) {
        val = _val;
        next = nullptr;
        random = nullptr;
    }
};


class Solution {
public:
    Node* copyRandomList(Node* head) {
        unordered_map<int, int> m;

        Node* head2 = head;

        Node* newhead = new Node(head->val);
        Node* curr = newhead;

        head2 = head2->next;

        // Init of new LL
        while(head2 != nullptr){
            curr->next = new Node(head2->val);
            head2 = head2->next;
            curr = curr->next;
        }   

        curr = newhead;
        
    }
};
