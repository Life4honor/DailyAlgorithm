package july.ninth;
import july.ninth.GetTheMiddelCharacter.GetTheMiddleCharacter;
import org.junit.Test;
import static org.junit.Assert.assertEquals;


public class GetTheMiddelCharacterTest {
    @Test
    public void evenTests() {
        assertEquals("es", GetTheMiddleCharacter.getMiddle("test"));
        assertEquals("dd", GetTheMiddleCharacter.getMiddle("middle"));
    }

    @Test
    public void oddTests() {
        assertEquals("t", GetTheMiddleCharacter.getMiddle("testing"));
        assertEquals("A", GetTheMiddleCharacter.getMiddle("A"));
    }

}
