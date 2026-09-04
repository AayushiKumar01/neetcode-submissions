public class Solution {
    public bool IsAnagram(string s, string t) {
        if (s.Length != t.Length){
            return false;
        }
        char[] c = s.ToCharArray();
        char[] d = t.ToCharArray();
        Array.Sort(c);
        Array.Sort(d);
        return c.SequenceEqual(d);
    }
}
