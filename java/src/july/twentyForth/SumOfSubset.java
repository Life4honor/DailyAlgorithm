package july.twentyForth;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.List;

public class SumOfSubset {
    public static int sum(int length, int expected, int[] inputs){
        List<int[]> ints = Arrays.asList(inputs);
        for (int[] anInt : ints) {
            for (int i : anInt) {
                System.out.println(i);
            }

        }

//        boolean condition = ;
        int result = 0;

        System.out.println(ints.toString());
        Collections.shuffle(ints);
        System.out.println(ints.toString());
//        if(condition)
//            result++;

        return result;
    }
}
