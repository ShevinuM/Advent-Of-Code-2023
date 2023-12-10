import java.util.ArrayList;
import java.util.HashSet;

public class Solution {

    /*
     * Any character that is a digit will be stored as a digit
     * A period is stored as -1
     * A gear is stored as -2
     * Any symbol is stored as -3
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
                    n = -1;
                } else if (Character.isDigit(c)) {
                    n = c - '0';
                } else if (c == '*') {
                    n = -2;
                } else {
                    n = -3;
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
            if ((i + 1 < pInput[ln].length && pInput[ln][i + 1] < -1) || (i - 1 >= 0 && pInput[ln][i - 1] < -1))
                return true;

            // check if adjacent vertically
            if ((ln + 1 < pInput.length && pInput[ln + 1][i] < -1) || (ln - 1 >= 0 && pInput[ln - 1][i] < -1))
                return true;

            // check diagonally
            if ((ln + 1 < pInput.length && i + 1 < pInput[ln].length && pInput[ln + 1][i + 1] < -1) ||
                    (ln - 1 >= 0 && i - 1 >= 0 && pInput[ln - 1][i - 1] < -1) ||
                    (ln + 1 < pInput.length && i - 1 >= 0 && pInput[ln + 1][i - 1] < -1) ||
                    (ln - 1 >= 0 && i + 1 < pInput[ln].length && pInput[ln - 1][i + 1] < -1))
                return true;
        }

        return false;
    }

    public static int getGearRatioSum(int[][] pInput) {
        int res = 0;
        for (int ln = 0; ln < pInput.length; ln++) {
            for (int i = 0; i < pInput[0].length; i++) {
                if (pInput[ln][i] != -2)
                    continue;
                HashSet<Integer> adjacent_gears = getAdjacentGears(new int[]{ln, i}, pInput);
                if (adjacent_gears.size() == 2) {
                    int gearRatio = 1;
                    for (int gear : adjacent_gears) {
                        gearRatio*=gear;
                    }
                    res += gearRatio;
                }
            }
        }
        return res;
    }

    /*
     * Inputs:
     * g_index = {y, x} index of the gear
     */
    public static HashSet<Integer> getAdjacentGears(int[] g_index, int[][] pInput) {
        HashSet<Integer> res = new HashSet<>();
        for (int x = -1; x <= 1; x++) {
            for (int y = -1; y <= 1; y++) {
                int newY = g_index[0] + y;
                int newX = g_index[1] + x;
                if (x == 0 && y == 0)
                    continue;
                if (newY >= 0 && newY < pInput.length && newX >= 0 && newX < pInput[0].length
                        && pInput[newY][newX] >= 0) {
                    int[] start = new int[] { newY, newX };
                    int[] end = new int[] { newY, newX };
                    while (start[1] > 0 && pInput[start[0]][start[1] - 1] >= 0)
                        start[1] = start[1] - 1;
                    while (end[1] < pInput[0].length - 1 && pInput[end[0]][end[1] + 1] >= 0)
                        end[1] = end[1] + 1;
                    if (start[1] == end[1]) {
                        res.add(pInput[start[0]][start[1]]);
                    } else {
                        int ln = start[0];
                        int part_num = 0;
                        for (int i = start[1]; i <= end[1]; i++) {
                            part_num = part_num * 10 + pInput[ln][i];
                        }
                        res.add(part_num);
                    }
                }
            }
        }
        return res;
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
