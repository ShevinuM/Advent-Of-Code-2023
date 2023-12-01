import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;

public class Main {

    public static void main(String[] args) {
        int res = 0;
        try {
            BufferedReader reader = new BufferedReader(new FileReader(args[0]));
            String line;
            while ((line = reader.readLine()) != null) {
                res += Sol.getCalbVal2(line);
            }
            reader.close();
        } catch (IOException e) {
            e.printStackTrace();
        }
        System.out.println(res);
    }

}