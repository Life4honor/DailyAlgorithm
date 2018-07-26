package july.twentyFirst;


import org.junit.Test;

import static org.junit.Assert.assertEquals;

public class HideAndSeekTest {
    @Test
    public void test() {
        assertEquals(4, HideAndSeek.seek(5, 17));
    }
}