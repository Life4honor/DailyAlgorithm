package august.first;

import org.junit.Test;

import static org.junit.Assert.assertEquals;

public class PalindromeTest {
    @Test
    public void isPalindromeChar(){
        assertEquals(false, Palindrome.isPalindromeChar("test"));
        assertEquals(true, Palindrome.isPalindromeChar("aba"));
    }
}
