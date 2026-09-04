class Solution {
    public boolean hasDuplicate(int[] nums) {
      HashSet<Integer> hashforDuplicates = new HashSet<Integer>();
      for (int num: nums){
      if (hashforDuplicates.contains(num)){
        return true;
      }  
      hashforDuplicates.add(num);
      }
      return false;
    }
}
