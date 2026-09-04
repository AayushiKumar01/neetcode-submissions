/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */

class Solution {
    public boolean hasCycle(ListNode head) {
        if(head.next == null){
            return false;
        }
        Set<ListNode> listSet = new HashSet<> ();
        while(head != null){
            if (listSet.contains(head)){
                return true;
            }
            listSet.add(head);
            head = head.next;
        }

       return false; 
    }
}
