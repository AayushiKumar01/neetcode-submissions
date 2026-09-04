class Solution {
    public boolean hasDuplicate(int[] nums) {
      Set<Integer> hashforDuplicates = new HashSet<>();
      for (int num: nums){
      if (hashforDuplicates.contains(num)){
        return true;
      }  
      hashforDuplicates.add(num);
      }
      return false;
    }
}
