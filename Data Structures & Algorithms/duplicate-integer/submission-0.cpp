class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        set<int> vals;
        for (int i = 0; i < nums.size(); ++i) {
            vals.insert(nums[i]);
        }
        if (vals.size() != nums.size()) {
            return true;
        }
        return false;
    }
};
