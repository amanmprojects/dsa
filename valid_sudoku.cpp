#include <vector>
#include <unordered_set>

using namespace std;

class Solution {
public:
    bool isValidSudoku(vector<vector<char>>& board) {
        // Row check
        for(vector<char> row: board){
            unordered_set<char> s;
            for(char c: row){
                if(c != '.' && s.count(c)) return false;
                s.insert(c);
            }
        }

        // Column check (i is row index, j is column index)
        int i,j;
        i = j = 0;

        for(; j < 9; j++){
            unordered_set<char> s;
            for(i = 0; i < 9; i++){
                if(board[i][j] != '.' && s.count(board[i][j])) return false;
                s.insert(board[i][j]);
            }
        }

        // 3x3 Grid check (a, i are row indexes and b, j are column indexes)
        int a, b;
        a = b = i = j = 0;

        for(; a < 9; a += 3){
            for(b = 0; b < 9; b += 3){
                unordered_set<char> s;
                for(i = a; i < (a+3); i++){
                    for(j = b; j < (b+3); j++){
                        if(board[i][j] != '.' && s.count(board[i][j])) return false;
                        s.insert(board[i][j]);
                    }
                }
            }
        }

        return true;
    }
};

vector<vector<vector<char>>> test_cases = {
    {{'1','2','.','.','3','.','.','.','.'},
 {'4','.','.','5','.','.','.','.','.',},
 {'.','9','8','.','.','.','.','.','.','3'},
 {'5','.','.','.','.','6','.','.','.','.','4'},
 {'.','.','.','.','8','.','.','3','.','.','.','.','5'},
 {'7','.','.','.','.','2','.','.','.','.','.','.','6'},
 {'.','.','.','.','.','.','.','.','.','2','.','.'},
 {'.','.','.','.','.','4','1','9','.','.','.','.','8'},
 {'.','.','.','.','.','.','8','.','.','.','.','7','9'}},
    {{'5','3','.','.','7','.','.','.','.'},
 {'6','.','.','1','9','5','.','.','.'},
 {'.','9','8','.','.','.','.','6','.'},
 {'8','.','.','.','6','.','.','.','3'},
 {'4','.','.','8','.','3','.','.','1'},
 {'7','.','.','.','2','.','.','.','6'},
 {'.','6','.','.','.','.','2','8','.'},
 {'.','.','.','4','1','9','.','.','5'},
 {'.','.','.','.','8','.','.','7','9'}}
};


int main(){
    for(vector<vector<char>>& t: test_cases){

    }
}

