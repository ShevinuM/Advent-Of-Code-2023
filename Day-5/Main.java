import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.ArrayList;

public class Main {

    public static void main(String[] args) {
        try {
            String input = Files.readString(Paths.get(args[0]));
            Solution solution = new Solution(input);
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

}