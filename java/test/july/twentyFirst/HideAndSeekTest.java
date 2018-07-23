package july.twentyFirst;


import org.junit.Test;

import java.util.Scanner;

import static org.junit.Assert.assertEquals;

public class HideAndSeekTest {

    @Test
    public void test() {
        System.out.println("longest Fixed Tests");
        assertEquals(4, HideAndSeek.seek(5, 17));
    }
}