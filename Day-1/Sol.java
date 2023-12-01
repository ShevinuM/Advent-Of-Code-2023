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
        System.out.println(getCalbVal(replace(args[0])));
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


    public static String replace(String input) {
        input = input.replace("one", "o 1 e");
        input = input.replace("two", "t 2 0");
        input = input.replace("three", "t 3 e");
        input = input.replace("four", "f 4 r");
        input = input.replace("five", "f 5 e");
        input = input.replace("six", "s 6 x");
        input = input.replace("seven", "s 7 n");
        input = input.replace("eight", "e 8 t");
        input = input.replace("nine", "n 9 e");
        return input;
    }
}
