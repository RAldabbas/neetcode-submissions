class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        HashMap<Integer, Integer> tempMap = new HashMap();
        int n = nums.length;
        List<Integer>[] buckets = new ArrayList[n + 1];
        for (int num : nums) {
            tempMap.putIfAbsent(num, 0);
            tempMap.put(num, tempMap.get(num) + 1);
        }

        for (int i = 0; i <= n; ++i) {
            buckets[i] = new ArrayList();
        }

        for (int key : tempMap.keySet()) {
            buckets[tempMap.get(key)].add(key);
        }

        List<Integer> allNums = new ArrayList();

        for (int i = n; i >= 0; --i) {
            for (int num : buckets[i]) {
                allNums.add(num);
            }
        }

        int[] returnList = new int[k];

        for (int i = 0; i < k; ++i) {
            returnList[i] = allNums.get(i);
        }

        return returnList;
    }
}
