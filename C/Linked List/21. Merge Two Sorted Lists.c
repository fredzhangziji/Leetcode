 // Definition for singly-linked list.
struct ListNode {
    int val;
    struct ListNode *next;
};
 


struct ListNode* mergeTwoLists(struct ListNode* list1, struct ListNode* list2){
    // edge cases
    if (!list1 && !list2) {
        return NULL;
    }
    if (!list1) {
        return list2;
    }
    if (!list2) {
        return list1;
    }
    
    struct ListNode list3;
    struct ListNode *tmp = &list3;
    while (list1 && list2) {
        if (list1->val <= list2->val) {
            tmp->next = list1;
            list1 = list1->next;
            tmp = tmp->next;
        } else {
            tmp->next = list2;
            list2 = list2->next;
            tmp = tmp->next;
        }
    }
    
    if (list1) {
        tmp->next = list1;
    }
    if (list2) {
        tmp->next = list2;
    }
    return list3.next;
}