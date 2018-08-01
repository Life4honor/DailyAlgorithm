package august.first;

public class Palindrome {
    public static boolean isPalindromeChar(String input){
        boolean result = true;
        for(int i=0; i < input.length()/2; i++){
            if(input.charAt(i) != input.charAt(input.length()-i-1)) {
                result = false;
            }
        }
        return result;
    }
}
