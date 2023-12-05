import java.util.Collections;
import java.util.HashMap;
import java.util.HashSet;
import java.util.TreeMap;
import java.util.TreeSet;
import java.util.concurrent.ConcurrentHashMap;
import java.util.concurrent.ConcurrentMap;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.util.concurrent.TimeUnit;

public class Solution {

    HashSet<Integer> seeds;
    HashSet<Integer> keySet;

    public Solution(String input) {
        this.seeds = new HashSet<>();
        this.keySet = new HashSet<>();
        this.processInput(input);
    }

    public void processInput(String input) {
        String[] segments = input.split("\n\\s*\n");
        // split the string into each section

        for (String segment : segments) {
            String[] parts = segment.split(":");

            if (parts[0].trim().equals("seeds")) {
                populateSeeds2(parts[1].trim().split(" "));
            } else {
                populateMap(parts[1].trim().split("\n"));
            }
        }
    }

    public int getLowestLocation() {
        return Collections.min(keySet);
    }

    public void populateSeeds(String[] seeds) {
        for (String seed : seeds) {
            this.seeds.add(Integer.parseInt(seed));
            this.keySet.add(Integer.parseInt(seed));
        }
    }

    public void populateSeeds2(String[] seeds) {
        for (int i = 0; i < seeds.length; i += 2) {
            final int index = i;
            int starts = Integer.parseInt(seeds[index]);
            int range = Integer.parseInt(seeds[index + 1]);
            for (int c = starts; c < starts + range; c++) {
                synchronized (this) {
                    this.seeds.add(c);
                    this.keySet.add(c);
                }
            }
        }
    }

    /*
     * Input
     * type = 'sts', 'htl', ....
     * mappings = ["50 98 2", "52 50 48"]
     * 
     * drs = destination range start
     * srs = source range start
     * rl = range length
     */
    public void populateMap(String[] mappings) {
        ConcurrentMap<Integer, Integer> map = new ConcurrentHashMap<>();
        ExecutorService executor = Executors.newFixedThreadPool(mappings.length);
        for (String mapping : mappings) {
            executor.submit(() -> {
                String[] entry = mapping.trim().split(" ");
                int rl = Integer.parseInt(entry[2]);
                for (int i = 0; i < rl; i++) {
                    final int index = i;

                    int source = Integer.parseInt(entry[1]) + index;
                    int destination = Integer.parseInt(entry[0]) + index;
                    if (keySet.contains(source))
                        map.put(source, destination);
                }
            });
        }
        executor.shutdown();
        try {
            executor.awaitTermination(Long.MAX_VALUE, TimeUnit.NANOSECONDS);
        } catch (InterruptedException e) {

        }
        HashSet<Integer> temp = new HashSet<>();
        for (int x : this.keySet) {
            int key = map.containsKey(x) ? map.get(x) : x;
            temp.add(key);
        }
        this.keySet.clear();
        this.keySet.addAll(temp);
        System.out.println(keySet);
    }
}
