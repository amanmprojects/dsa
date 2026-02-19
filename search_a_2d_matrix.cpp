class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        pair<int, int> dims;
        dims.first = matrix.size(); //Rows
        dims.second = matrix[0].size(); // Columns
        int total = dims.first * dims.second;

        int l, r, mid, i, j;
        l = 0;
        r = (dims.first * dims.second)-1;

        while(l <= r) {
            mid = (l + r) / 2;
            i = mid / dims.first;
            j = mid % dims.first;
            if(matrix[i][j] == target) return true;
            else if(matrix[i][j] < target) l = mid+1;
            else r = mid - 1;
        }

        return false;
     }
};
