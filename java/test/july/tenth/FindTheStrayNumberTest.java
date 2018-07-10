package july.tenth;

import july.tenth.FindTheStrayNumber.FindTheStrayNumber;
import org.junit.Test;
import static org.junit.Assert.assertEquals;

public class FindTheStrayNumberTest {

    @Test
    public void simpleArray1() {
        assertEquals(2, getActualFor(1, 1, 2));
    }

    private int getActualFor(int... numbers) {
        return FindTheStrayNumber.stray(numbers);
    }
}
