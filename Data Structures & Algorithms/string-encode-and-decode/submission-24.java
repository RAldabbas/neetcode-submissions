class Solution {

    public String encode(List<String> strs) {
        StringBuilder result = new StringBuilder();
        for (int i = 0; i < strs.size(); ++i) {
            String tempStr = strs.get(i);
            if (tempStr.isEmpty()) {
                result.append(',');
            } else {
                for (char c : tempStr.toCharArray()) {
                    result.append(c - 'a').append(',');
                }
            }
            if (i != strs.size() - 1) {
                result.append('|');
            }
        }
        return result.toString();
    }

    public List<String> decode(String str) {
        List<String> returnList = new ArrayList();

        if (str.isEmpty()) {
            return returnList;
        }

        String[] splitStr = str.split("\\|");
        for (String tempStr : splitStr) {
            if (tempStr.equals(',')) {
                returnList.add("");
                continue;
            }
            StringBuilder newWord = new StringBuilder();
            String[] newStuff = tempStr.split(",");
            for (String letter : newStuff) {
                if (!letter.isEmpty()) {
                    int letterIndex = Integer.parseInt(letter);
                    newWord.append((char) (letterIndex + 'a'));
                }
            }
            returnList.add(newWord.toString());
        }
        return returnList;
    }
}
