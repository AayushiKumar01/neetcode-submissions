class Solution {
    public int[] topKFrequent(int[] nums, int k) {

      Map<Integer, Integer> freqMap = new HashMap<> ();
      for (int num: nums){
        freqMap.put(num, freqMap.getOrDefault(num,0) + 1);
      }  

      List<Integer>[] bucket= new List[nums.length + 1];
      freqMap.forEach((num,freq) -> {
        if(bucket[freq] == null){
            bucket[freq] = new ArrayList<>();
        }
        bucket[freq].add(num);
      }); 
        List<Integer> res =  new ArrayList<> ();
      for (int i = bucket.length - 1; i > 0 && res.size() < k; i--){
        if(bucket[i] != null){
            res.addAll(bucket[i]);
        }
      }
      return res.stream().mapToInt(i -> i).toArray();
    }
}
