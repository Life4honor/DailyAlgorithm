package july.ninth.GetTheMiddelCharacter;

public class GetTheMiddleCharacter {
    public static String getMiddle(String word) {
        //Code goes here!
        StringBuffer result = new StringBuffer();
        if(word.length()%2==0){
            result.append(word.charAt(word.length()/2));
            result.append(word.charAt(word.length()/2 +1));
        }else{
            result.append(word.charAt(word.length()/2));
        }

        return result.toString();
    }
}
