package july.tenth.FindTheStrayNumber;

import java.util.ArrayList;
import java.util.List;

public class FindTheStrayNumber {
    public static int stray(int[] numbers) {
        int result = 0;
        List<Integer> intList = new ArrayList<>();
        for (int number : numbers) {
            intList.add(number);
        }
        for (int number : numbers) {
            if(intList.indexOf(number) == intList.lastIndexOf(number))
                result = number;
        }

        return result;
    }
}
