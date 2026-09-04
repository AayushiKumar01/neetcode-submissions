class Solution {
    public int[] twoSum(int[] nums, int target) {
        Map<Integer,Integer> checkSum = new HashMap<Integer,Integer> ();
        for (int i =0; i< nums.length; i++){
            if(checkSum.containsKey(target-nums[i])){
                return new int[] {checkSum.get(target-nums[i]),i};
            }
            checkSum.put(nums[i],i);
        }
        return new int[] {};
    }
}
