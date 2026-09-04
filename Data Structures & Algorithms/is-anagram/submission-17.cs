public class Solution {
    public bool IsAnagram(string s, string t) {
        if (s.Length != t.Length){
            return false;
        }
        // char[] c = s.ToCharArray();
        // char[] d = t.ToCharArray();
        // Array.Sort(c);
        // Array.Sort(d);
        // return c.SequenceEqual(d);

        //Better Solution

        int [] charCount = new int[26];
        foreach(char c in s){
            charCount[c - 'a']++;
        }

        foreach(char c in t){
            charCount[c - 'a']--;
        }

        foreach(int i in charCount){
            if (i != 0){
                return false;
            }
        }

        return true;
    }
}
