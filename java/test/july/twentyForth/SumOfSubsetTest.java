package july.twentyForth;

import org.junit.Test;

import static org.junit.Assert.assertEquals;

public class SumOfSubsetTest {
    @Test
    public void test(){
        int length = 5;
        int expected = 0;
        int[] inputs = {-7, -3, -2, 5, 8};
        assertEquals(1, SumOfSubset.sum(length, expected, inputs));
    }

}
