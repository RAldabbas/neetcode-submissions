class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        map<int, int> maps;
         // val, index
        for (int i = 0; i < nums.size(); ++i) {
            if (maps.find(target - nums[i]) != maps.end()) {
                int difference = target - nums[i];
                return {maps[difference], i};
            }
            maps.insert({nums[i], i});
        }
        return {};
    }
};
