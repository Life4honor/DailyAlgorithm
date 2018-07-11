package july.eleventh.YourOrderPlease;

import java.util.HashMap;
import java.util.Map;

public class YourOrderPlease {
    public static String order(String words) {
        if(words.equals(""))
            return "";
        String[] strings = words.split(" ");
        Map stringMap = new HashMap();
        for (String string : strings) {
            for(Integer i = 1; i<10; i++){
                if(string.contains(i.toString()))
                    stringMap.put(i.toString(),string);
            }
        }

        StringBuilder stringBuilder = new StringBuilder();
        for(Integer i = 1; i <= stringMap.size(); i++)
            stringBuilder.append(stringMap.get(i.toString())).append(" ");

        stringBuilder.deleteCharAt(stringBuilder.length()-1);
        return stringBuilder.toString();
    }
}
