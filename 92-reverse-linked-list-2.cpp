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
    ListNode* reverseBetween(ListNode* head, int left, int right) {
        if (head->next == nullptr)
        {
            return head;
        }
        if (left == right)
        {
            return head;
        }

        ListNode* outsideLeftPtr = nullptr;
        ListNode* currPtr = head;
        ListNode* prevPtr = nullptr;
        ListNode* nextPtr = head->next;
        int count = 1;

        while (count != left)
        {
            prevPtr = currPtr;
            currPtr = nextPtr;
            nextPtr = currPtr->next;
            count += 1;

        }
        outsideLeftPtr = prevPtr;

        prevPtr = nullptr;
        while (count != right)
        {
            currPtr->next = prevPtr;
            prevPtr = currPtr;
            currPtr = nextPtr;
            nextPtr = currPtr->next;
            count += 1;
        }

        currPtr->next = prevPtr;
        if (outsideLeftPtr != nullptr)
        {
            ListNode* leftPtr = outsideLeftPtr->next;
            outsideLeftPtr->next = currPtr;
            leftPtr->next = nextPtr;
        }
        else
        {
            head->next = nextPtr;
        }
        

        if (left == 1)
        {
            return currPtr;
        }
        else
        {
            return head;
        }
    }
};