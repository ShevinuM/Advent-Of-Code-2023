import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.HashMap;

public class Main {

    public static void main(String[] args) {
        int res = 0;
        int power_sum = 0;
        int id = 1;
        try {
            BufferedReader reader = new BufferedReader(new FileReader(args[0]));
            String line;
            while ((line = reader.readLine()) != null) {
                HashMap<Character, Integer> pInput = Solution.processInput(line);
                res += Solution.isPossible(pInput) ? id : 0;
                power_sum += Solution.sumOfThePower(pInput);
                id++;
            }
            reader.close();
        } catch (IOException e) {
            e.printStackTrace();
        }
        System.out.println("Part 1 -> " + res);
        System.out.println("Part 2 -> " + power_sum);
    }

}