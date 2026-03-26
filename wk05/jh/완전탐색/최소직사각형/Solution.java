package wk05.jh.완전탐색.최소직사각형;

class Solution {
    public int solution(int[][] sizes) {
        int answerS = 0;
        int answerL = 0;
        int testS = 0;
        int testL = 0;
        for(int i = 0; i < sizes.length; i++){
            if(sizes[i][0] <= sizes[i][1]){
                testS = sizes[i][0];
                testL = sizes[i][1];
            }else{
                testS = sizes[i][1];
                testL = sizes[i][0];
            }
            if(i == 0){
                answerS = testS;
                answerL = testL;
            }else{
                if(testS > answerS){
                    answerS = testS;
                }
                if(testL > answerL) {
                    answerL = testL;
                }
            }
        }
        return answerS * answerL;
    }
}