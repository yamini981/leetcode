/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* reverseList(ListNode* head) {
        if (head == nullptr)
        {
            return nullptr;
        }
        if (head->next == nullptr)
        {
            return head;
        }


        ListNode* currPtr = head;
        ListNode* prevPtr = nullptr;
        ListNode* nextPtr = head->next;

        while (nextPtr != nullptr)
        {
            currPtr->next = prevPtr;
            prevPtr = currPtr;
            currPtr = nextPtr;
            nextPtr = currPtr->next;
        }

        currPtr->next = prevPtr;

        return currPtr;
    }
};