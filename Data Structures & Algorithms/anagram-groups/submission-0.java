class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        Map<String, List<String>> map = new HashMap<String, List<String>>();
        List test1 = new ArrayList<>();
        
        for (String word : strs) {
            String sortedWord = insertionSort(word);
            if (!map.containsKey(sortedWord)) {
                map.put(sortedWord, new ArrayList<>());
            }
            map.get(sortedWord).add(word);
        }
        for (String key : map.keySet()) {
            test1.add(map.get(key));
        }
        return test1;
    }

    public String insertionSort(String word) {
        char[] chars = word.toCharArray();
        for (int i = 1; i < word.length(); ++i) {
            char key = chars[i];
            int j = i - 1;
            while (j >= 0 && chars[j] > key) {
                chars[j + 1] = chars[j];
                j--;
            }
            chars[j + 1] = key;
        }
        return new String(chars);
    }
}
