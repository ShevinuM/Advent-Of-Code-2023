import java.util.ArrayList;
import java.util.HashMap;
import java.util.HashSet;
import java.util.Map;

public class Solution {

    private HashMap<Integer, HashSet<Integer>> winning_numbers;
    private HashMap<Integer, HashSet<Integer>> my_numbers;
    private HashMap<Integer, Integer> no_of_copies;

    public Solution(ArrayList<String> input) {
        this.winning_numbers = new HashMap<>();
        this.my_numbers = new HashMap<>();
        this.no_of_copies = new HashMap<>();
        this.processInput(input);
    }

    public void processInput(ArrayList<String> input) {
        for (String card : input) {
            // card -> Card 1: 41 48 83 86 17 | 83 86 6 31 17 9 48 53
            String p_card = card.replaceFirst("Card\\s*", "");
            // card -> 1: 41 48 83 86 17 | 83 86 6 31 17 9 48 53
            String[] parts = p_card.split(":|\\|");
            // card -> ["1", " 41 48 83 86 17 ", " 83 86 6 31 17 9 48 53"]
            int card_no = Integer.parseInt(parts[0].trim()); // 1
            String[] winning_numbers_str = parts[1].trim().split("\\s+"); // ["41", "48", "83", ...]
            String[] my_numbers_str = parts[2].trim().split("\\s+"); // ["83", "86", "6",.....]
            HashSet<Integer> winning_numbers = new HashSet<>();
            HashSet<Integer> my_numbers = new HashSet<>();
            for (String c : winning_numbers_str)
                winning_numbers.add(Integer.parseInt(c));
            for (String c : my_numbers_str)
                my_numbers.add(Integer.parseInt(c));
            this.winning_numbers.put(card_no, winning_numbers);
            this.my_numbers.put(card_no, my_numbers);
            this.no_of_copies.put(card_no, 1);
        }
    }

    public int calculatePoints() {
        int res = 0;
        for (Map.Entry<Integer, HashSet<Integer>> entry : this.my_numbers.entrySet()) {
            int sum = 0;
            int count = 0;
            int card_no = entry.getKey();
            HashSet<Integer> numbers = entry.getValue();
            for (int number : numbers) {
                if (this.winning_numbers.get(card_no).contains(number)) {
                    sum = count == 0 ? 1 : sum * 2;
                    count++;
                }
            }
            res += sum;
        }
        return res;
    }

    public int getNoOfMatchingNumbers(int card_no) {
        int count = 0;
        HashSet<Integer> numbers = this.my_numbers.get(card_no);
        for (int number : numbers) {
            if (this.winning_numbers.get(card_no).contains(number))
                count++;
        }
        return count;
    }

    public void processScratchCards() {
        for (int card_no : this.my_numbers.keySet()) {
            for (int c = 0; c < this.no_of_copies.get(card_no); c++) {
                int match_count = getNoOfMatchingNumbers(card_no);
                for (int i = card_no + 1; i <= card_no + match_count; i++) {
                    this.no_of_copies.put(i, this.no_of_copies.get(i)+1);
                }
            }
        }
    }

    public int getTotalNumberOfScratchCards() {
        processScratchCards();
        int res = 0;
        for (int card_no : this.my_numbers.keySet()) {
            res += this.no_of_copies.get(card_no);
        }
        return res;
    }

    public void printMaps() {
        System.out.println("Winning Numbers");
        for (Map.Entry<Integer, HashSet<Integer>> entry : this.winning_numbers.entrySet()) {
            System.out.println("Card : " + entry.getKey());
            System.out.println(entry.getValue().toString());
        }
        System.out.println("");
        System.out.println("My Numbers");
        for (Map.Entry<Integer, HashSet<Integer>> entry : this.my_numbers.entrySet()) {
            System.out.println("Card : " + entry.getKey());
            System.out.println(entry.getValue().toString());
        }
    }
}
