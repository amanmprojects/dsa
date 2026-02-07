#include <vector>
#include <iostream>

using namespace std;

class Solution {
public:
    int trap(vector<int>& height) {
        int leftmax, rightmax, total;
        leftmax = rightmax = total = 0;

        for(int i = 1; i < height.size(); i++){
            if(height[i] > rightmax) rightmax = height[i];
        }

        for(int h: height){
            
        }
    }
};
