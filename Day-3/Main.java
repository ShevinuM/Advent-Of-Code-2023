import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;

public class Main {

    public static void main(String[] args) {
        int part1 = 0;
        ArrayList<String> input = new ArrayList<>();
        try {
            BufferedReader reader = new BufferedReader(new FileReader(args[0]));
            String line;
            while ((line = reader.readLine()) != null) {
                input.add(line);
            }
            int[][] pInput = new int[input.get(0).length()][input.size()];
            pInput = Solution.processInput(input);
            part1 = Solution.getPartSum(pInput);
            reader.close();
        } catch (IOException e) {
            e.printStackTrace();
        }
        System.out.println("Part 1 -> " + part1);
    }

}