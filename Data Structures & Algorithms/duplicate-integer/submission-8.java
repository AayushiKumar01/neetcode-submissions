class Solution {
    public boolean hasDuplicate(int[] nums) {
        Set<Integer> nonDuplicates = new HashSet<Integer> ();
        for(int num: nums){
            if (nonDuplicates.contains(num)){
                return true;
            }
            nonDuplicates.add(num);
        }
        return false;
    }
}