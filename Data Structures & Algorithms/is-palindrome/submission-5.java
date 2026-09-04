class Solution {
    public boolean isPalindrome(String s) {
       int start = 0;
       int end = s.length()-1;

       String lowerCase = s.toLowerCase();

       while(start < end){
        while(start < end && !Character.isLetterOrDigit(lowerCase.charAt(start))){
            start++;
        }
        while(start < end && !Character.isLetterOrDigit(lowerCase.charAt(end))){
            end --;
        }
        if(lowerCase.charAt(start) != lowerCase.charAt(end)){
            return false;
        }

        start++;
        end--;
       }

       return true;
    }
}
