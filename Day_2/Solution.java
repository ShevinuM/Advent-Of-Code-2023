import java.util.HashMap;
import java.util.Map;

public class Solution {
    static int MAX_R = 12;
    static int MAX_G = 13;
    static int MAX_B = 14;

    public static boolean isPossible(HashMap<Character, Integer> data) {
        for (Map.Entry<Character, Integer> entry : data.entrySet()) {
            Character key = entry.getKey();
            Integer value = entry.getValue();
            switch (key) {
                case 'r':
                    if (value > MAX_R)
                        return false;
                    break;
                case 'g':
                    if (value > MAX_G)
                        return false;
                    break;
                case 'b':
                    if (value > MAX_B)
                        return false;
                    break;
            }
        }
        return true;
    }

    public static int sumOfThePower(HashMap<Character, Integer> data) {
        int res = 1;
        for (Map.Entry<Character, Integer> entry : data.entrySet()) {
            res *= entry.getValue();
        }
        return res;
    }

    public static HashMap<Character, Integer> processInput(String input) {
        HashMap<Character, Integer> res = new HashMap<>();
        res.put('r', 0);
        res.put('g', 0);
        res.put('b', 0);
        // input -> Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
        String pInput = input.replaceFirst("Game \\d+: ", "");
        // pInput -> 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
        pInput = pInput.replaceAll("\\s", "");
        // pInput -> 3blue,4red;1red,2green,6blue;2green
        String[] sets = pInput.split(";");
        // sets -> ["3blue,4red", "1red,2green", "6blue;2green"]
        for (String set : sets) {
            // set -> 3blue,4red
            String[] cubes = set.split(",");
            // cubes -> ["3blue", "4red"]
            for (String cube : cubes) {
                String[] parts = cube.split("(?<=\\d)(?=\\D)");
                int number = Integer.parseInt(parts[0]);
                if (parts[1].equals("blue")) {
                    if (number > res.get('b'))
                        res.put('b', number);
                } else if (parts[1].equals("red")) {
                    if (number > res.get('r'))
                        res.put('r', number);
                } else {
                    if (number > res.get('g'))
                        res.put('g', number);
                }
            }
        }
        return res;
    }
}
