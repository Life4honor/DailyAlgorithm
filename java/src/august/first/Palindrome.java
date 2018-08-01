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

    public static boolean isPalindromeString(String input){
        return input.substring(0, input.length() / 2).equals(input.substring(input.length() / 2));
    }

    public static void main(String[] args) {
        System.out.println(isPalindromeChar("test"));
        System.out.println(isPalindromeChar("teetteet"));
        System.out.println(isPalindromeString("test"));
        System.out.println(isPalindromeString("teetteet"));
    }
}
