package july.sixteenth;

import java.util.ArrayList;
import java.util.List;

public class FindTheParityOutlier {
    static int find(int[] integers) {

        List<Integer> oddNumber = new ArrayList<>();
        List<Integer> evenNumber = new ArrayList<>();

        for (int integer : integers) {
            if(integer%2==0)
                evenNumber.add(integer);
            else
                oddNumber.add(integer);
        }

        if(evenNumber.size()>oddNumber.size())
            return oddNumber.get(0);
        else
            return evenNumber.get(0);
    }
}
