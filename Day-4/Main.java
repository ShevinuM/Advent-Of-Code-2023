import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;

public class Main {

    public static void main(String[] args) {
        ArrayList<String> input = new ArrayList<>();
        try {
            BufferedReader reader = new BufferedReader(new FileReader(args[0]));
            String line;
            while ((line = reader.readLine()) != null) {
                input.add(line);
            }
            Solution solution = new Solution(input);
            System.out.println("Part 1 -> " + solution.calculatePoints());
            System.out.println("Part 2 -> " + solution.getTotalNumberOfScratchCards());
            reader.close();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

}