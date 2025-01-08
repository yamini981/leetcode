class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
        string currentLongestPrefix = strs[0];
        for (int i = 1; i < strs.size(); i++) {
            if (currentLongestPrefix == "") {
                break;
            }
            if (strs[i] == currentLongestPrefix) {
                //do nothing
            }
            else {
                int stringLength = currentLongestPrefix.length();
                if (stringLength > strs[i].length()) {
                    stringLength = strs[i].length();
                }
                
                string bufferLongestPrefix = "";
                for (int charIndex = 0; charIndex < stringLength; charIndex++) {
                    if (currentLongestPrefix[charIndex] == strs[i][charIndex]) {
                        bufferLongestPrefix += currentLongestPrefix[charIndex];
                    }
                    else {
                        break;
                    }
                    
                }
                currentLongestPrefix = bufferLongestPrefix;
            }
        }
        return currentLongestPrefix;
    }
};