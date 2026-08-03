class Solution {
    public int solution(int[] absolutes, boolean[] signs) {
        int ans = 0;
        int L = absolutes.length;
        for (int i=0;i<L;i++) {
            if (signs[i]) ans+=absolutes[i];
            else ans-=absolutes[i];
        }
        return ans;
    }
}