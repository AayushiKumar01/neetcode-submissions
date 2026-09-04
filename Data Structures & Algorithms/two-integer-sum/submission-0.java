class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer, Integer> pair = new HashMap<> ();
        for (int i = 0; i < nums.length; i++){
            if (pair.containsKey(target - nums[i])){
                return new int[]{pair.get(target - nums[i]), i};
            }
            pair.put(nums[i],i);
        }
        return new int[]{};
    }
    
}
