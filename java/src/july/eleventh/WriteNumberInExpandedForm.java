package july.eleventh;

import java.util.ArrayList;
import java.util.List;

public class WriteNumberInExpandedForm {
    public static String expandedForm(int num)
    {
        //your code here
        String numStr = Integer.valueOf(num).toString();
        List<Integer> intList = new ArrayList<>();
        for(int i = numStr.length()-1; i>=0; i--){
            Integer deonominator = Integer.valueOf((int)Math.pow(10,i));
            Integer quotient = num/deonominator;
            if(quotient>0)
                intList.add(quotient*deonominator);
            num = num - deonominator*quotient;
        }
        System.out.println(intList);
        StringBuilder resultStr = new StringBuilder();
        for (Integer integer : intList) {
            resultStr.append(integer);
            resultStr.append(" + ");
        }
        resultStr.delete(resultStr.length()-3, resultStr.length());
        return resultStr.toString();
    }
}
