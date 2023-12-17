import java.util.HashMap;
import java.util.HashSet;
import java.util.TreeMap;
import java.util.TreeSet;

public class p1 {

    HashSet<Long> seeds;
    HashMap<Long, Long> map;
    TreeSet<Long> keySet;

    public p1(String input) {
        this.seeds = new HashSet<>();
        this.map = new HashMap<>();
        this.keySet = new TreeSet<>();
        this.processInput(input);
    }

    public void processInput(String input) {
        String[] segments = input.split("\n\\s*\n");
        // split the string into each section

        for (String segment : segments) {
            String[] parts = segment.split(":");

            if (parts[0].trim().equals("seeds")) {
                populateSeeds(parts[1].trim().split(" "));
            } else {
                populateMap(parts[1].trim().split("\n"));
            }
        }
    }

    public long getLowestLocation() {
        return this.keySet.first();
    }

    public void populateSeeds(String[] seeds) {
        for (String seed : seeds) {
            this.seeds.add(Long.parseLong(seed));
            this.keySet.add(Long.parseLong(seed));
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
        map.clear();
        long drs = 0, srs = 0, rl = 0;
        for (String mapping : mappings) {
            String[] entry = mapping.trim().split(" ");
            drs = Long.parseLong(entry[0]);
            srs = Long.parseLong(entry[1]);
            rl = Long.parseLong(entry[2]);
            for (long i = 0; i < rl; i++) {
                long source = srs + i;
                long destination = drs + i;
                if (keySet.contains(source))
                    map.put(source, destination);
            }
        }
        TreeSet<Long> temp = new TreeSet<>();
        for (long x : this.keySet) {
            long key = map.containsKey(x) ? map.get(x) : x;
            temp.add(key);
        }
        this.keySet.clear();
        this.keySet.addAll(temp);
        System.out.println(keySet);
    }
}
