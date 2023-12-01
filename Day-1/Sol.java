import java.util.Arrays;
import java.util.HashMap;
import java.util.HashSet;
import java.util.Map;
import java.util.Set;

public class Sol {

    /*
     * 1. Create an array of size 2
     * 2. Iterate through the input
     * 3. Add the first number in the input to the first index of the array
     * 4. Add the second number in the input to the second index of the array
     * 5. After the input has been fully iterated first input should be the first
     * digit and second index should be the last digit
     * 6. Return arr[0] * 10 + arr[1]
     */

    public static void main(String[] args) {
        System.out.println(getCalbVal2(args[0]));
    }

    public static int getCalbVal(String input) {
        Integer[] arr = new Integer[2];
        boolean started = false;
        char[] c_arr = input.toCharArray();
        for (char c : c_arr) {
            if (Character.isDigit(c))
                if (!started) {
                    arr[0] = c - '0';
                    arr[1] = c - '0';
                    started = true;
                } else {
                    arr[1] = c - '0';
                }
        }
        if (arr[0] == null)
            return 0;

        return arr[0] * 10 + arr[1];
    }

    public static int getCalbVal2(String input) {
        HashMap<Integer, String[]> numbers = new HashMap<>();
        numbers.put(3, new String[] { "two", "one", "six" });
        numbers.put(4, new String[] { "four", "five", "nine" });
        numbers.put(5, new String[] { "three", "seven", "eight" });

        Map<String, Integer> stringToNumber = new HashMap<>();
        stringToNumber.put("zero", 0);
        stringToNumber.put("one", 1);
        stringToNumber.put("two", 2);
        stringToNumber.put("three", 3);
        stringToNumber.put("four", 4);
        stringToNumber.put("five", 5);
        stringToNumber.put("six", 6);
        stringToNumber.put("seven", 7);
        stringToNumber.put("eight", 8);
        stringToNumber.put("nine", 9);

        Integer[] arr = new Integer[2];
        boolean started = false;
        char[] c_arr = input.toCharArray();
        for (int i = 0; i < c_arr.length; i++) {
            char c = c_arr[i];
            if (Character.isDigit(c))
                if (!started) {
                    arr[0] = c - '0';
                    arr[1] = c - '0';
                    started = true;
                } else {
                    arr[1] = c - '0';
                }
            else {
                for (int l = 3; l <= 5; l++) {
                    if (i + l > c_arr.length)
                        break;
                    String subStr = input.substring(i, i + l);
                    String[] elements = numbers.get(l);
                    for (String element : elements) {
                        if (element.equals(subStr)) {
                            if (!started) {
                                arr[0] = stringToNumber.get(subStr);
                                arr[1] = stringToNumber.get(subStr);
                                started = true;
                            } else {
                                arr[1] = stringToNumber.get(subStr);
                            }
                        }
                    }
                }
            }
        }
        
        if (arr[0] == null)
            return 0;

        return arr[0] * 10 + arr[1];
    }
}
