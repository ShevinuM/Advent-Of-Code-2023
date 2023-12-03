import java.util.ArrayList;

public class Solution {

    /*
     * Any character that is a digit will be stored as a digit
     * A period is stored as -2
     * Any symbol is stored as -1
     */
    public static int[][] processInput(ArrayList<String> input) {

        final int no_of_characters = input.get(0).length();
        final int no_of_lines = input.size();

        int[][] res = new int[no_of_lines][no_of_characters];

        for (int ln = 0; ln < no_of_lines; ln++) {
            String line = input.get(ln);
            for (int i = 0; i < no_of_characters; i++) {
                char c = line.charAt(i);
                int n;
                if (c == '.') {
                    n = -2;
                } else if (Character.isDigit(c)) {
                    n = c - '0';
                } else {
                    n = -1;
                }
                res[ln][i] = n;
            }
        }
        return res;
    }

    public static int getPartSum(int[][] pInput) {
        int res = 0;
        for (int ln = 0; ln < pInput.length; ln++) {
            for (int i = 0; i < pInput[0].length; i++) {
                if (pInput[ln][i] < 0)
                    continue;
                int part_num = pInput[ln][i];
                ArrayList<Integer> indices = new ArrayList<>();
                indices.add(i);
                while (i + 1 < pInput[ln].length && pInput[ln][i + 1] >= 0) {
                    i++;
                    indices.add(i);
                    part_num = part_num * 10 + pInput[ln][i];
                }
                res += isAdjacent(pInput, ln, indices) ? part_num : 0;
            }
        }
        return res;
    }

    public static boolean isAdjacent(int[][] pInput, int ln, ArrayList<Integer> indices) {

        for (int i : indices) {
            // check if adjacent horizontally
            if ((i + 1 < pInput[ln].length && pInput[ln][i + 1] == -1) || (i - 1 >= 0 && pInput[ln][i - 1] == -1))
                return true;

            // check if adjacent vertically
            if ((ln + 1 < pInput.length && pInput[ln + 1][i] == -1) || (ln - 1 >= 0 && pInput[ln - 1][i] == -1))
                return true;

            if ((ln + 1 < pInput.length && i + 1 < pInput[ln].length && pInput[ln + 1][i + 1] == -1) ||
                    (ln - 1 >= 0 && i - 1 >= 0 && pInput[ln - 1][i - 1] == -1) ||
                    (ln + 1 < pInput.length && i - 1 >= 0 && pInput[ln + 1][i - 1] == -1) ||
                    (ln - 1 >= 0 && i + 1 < pInput[ln].length && pInput[ln - 1][i + 1] == -1))
                return true;
        }

        return false;
    }

    public static void print(int[][] pInput) {
        for (int[] row : pInput) {
            for (int num : row) {
                System.out.print(num + " ");
            }
            System.out.println();
        }
    }

}
