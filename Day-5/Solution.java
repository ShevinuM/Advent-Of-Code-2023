import java.util.Arrays;
import java.util.HashMap;
import java.util.HashSet;
import java.util.TreeMap;

public class Solution {

    HashMap<Long, Long> seeds;
    HashMap<Long, Long> seed_to_soil_map;
    HashMap<Long, Long> soil_to_fertilizer_map;
    HashMap<Long, Long> fertilizer_to_water_map;
    HashMap<Long, Long> water_to_light_map;
    HashMap<Long, Long> light_to_temperature_map;
    HashMap<Long, Long> temperature_to_humidity_map;
    HashMap<Long, Long> humidity_to_location_map;
    TreeMap<Long, Long> location_to_seed_map;

    public Solution(String input) {
        this.seeds = new HashMap<>();
        this.seed_to_soil_map = new HashMap<>();
        this.soil_to_fertilizer_map = new HashMap<>();
        this.fertilizer_to_water_map = new HashMap<>();
        this.water_to_light_map = new HashMap<>();
        this.light_to_temperature_map = new HashMap<>();
        this.temperature_to_humidity_map = new HashMap<>();
        this.humidity_to_location_map = new HashMap<>();
        this.location_to_seed_map = new TreeMap<>();
        this.processInput(input);
        this.populateLocationtoSeedMap();
    }

    public void processInput(String input) {
        String[] segments = input.split("\n\\s*\n");
        // split the string into each section

        for (String segment : segments) {
            String[] parts = segment.split(":");
            switch (parts[0].trim()) {
                case "seeds":
                    populateSeeds(parts[1].trim().split(" "));
                    break;
                case "seed-to-soil map":
                    populateMaps("sts", parts[1].trim().split("\n"));
                    break;
                case "soil-to-fertilizer map":
                    populateMaps("stf", parts[1].trim().split("\n"));
                    break;
                case "fertilizer-to-water map":
                    populateMaps("ftw", parts[1].trim().split("\n"));
                    break;
                case "water-to-light map":
                    populateMaps("wtl", parts[1].trim().split("\n"));
                    break;
                case "light-to-temperature map":
                    populateMaps("ltt", parts[1].trim().split("\n"));
                    break;
                case "temperature-to-humidity map":
                    populateMaps("tth", parts[1].trim().split("\n"));
                    break;
                case "humidity-to-location map":
                    populateMaps("htl", parts[1].trim().split("\n"));
                    break;
            }
        }
    }

    public long getLowestLocation() {
        return location_to_seed_map.firstKey();
    }

    public void populateLocationtoSeedMap() {
        for (Long seed : this.seeds.keySet()) {
            long key = seed_to_soil_map.containsKey(seed) ? seed_to_soil_map.get(seed) : seed;
            key = soil_to_fertilizer_map.containsKey(key) ? soil_to_fertilizer_map.get(key) : key;
            key = fertilizer_to_water_map.containsKey(key) ? fertilizer_to_water_map.get(key) : key;
            key = water_to_light_map.containsKey(key) ? water_to_light_map.get(key) : key;
            key = light_to_temperature_map.containsKey(key) ? light_to_temperature_map.get(key) : key;
            key = temperature_to_humidity_map.containsKey(key) ? temperature_to_humidity_map.get(key) : key;
            key = humidity_to_location_map.containsKey(key) ? humidity_to_location_map.get(key) : key;
            location_to_seed_map.put(key, seed);
        }
    }

    public void populateSeeds(String[] seeds) {
        for (String seed : seeds)
            this.seeds.put(Long.parseLong(seed), Long.parseLong(seed));
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
    public void populateMaps(String type, String[] mappings) {
        long drs = 0, srs = 0, rl = 0;
        for (String mapping : mappings) {
            String[] entry = mapping.trim().split(" ");
            drs = Long.parseLong(entry[0]);
            srs = Long.parseLong(entry[1]);
            rl = Long.parseLong(entry[2]);
            for (long i = 0; i < rl; i++) {
                long source = srs + i;
                long destination = drs + i;
                switch (type) {
                    case "sts":
                        seed_to_soil_map.put(source, destination);
                        for (Long seed : this.seeds.keySet()) {
                            long value = seed_to_soil_map.containsKey(seed) ? seed_to_soil_map.get(seed) : seed;
                            this.seeds.put(value, value);
                        }
                        seed_to_soil_map = null;
                        System.gc();
                        break;
                    case "stf":
                        soil_to_fertilizer_map.put(source, destination);
                        for (Long seed : this.seeds.keySet()) {
                            long value = soil_to_fertilizer_map.containsKey(seed) ? soil_to_fertilizer_map.get(seed) : seed;
                            this.seeds.put(seed, value);
                        }
                        break;
                    case "ftw":
                        fertilizer_to_water_map.put(source, destination);
                        break;
                    case "wtl":
                        water_to_light_map.put(source, destination);
                        break;
                    case "ltt":
                        light_to_temperature_map.put(source, destination);
                        break;
                    case "tth":
                        temperature_to_humidity_map.put(source, destination);
                        break;
                    case "htl":
                        humidity_to_location_map.put(source, destination);
                        break;
                }
            }
        }
    }

    public void printMaps() {
        System.out.println("seed_to_soil_map: " + this.seed_to_soil_map);
        System.out.println("soil_to_fertilizer_map: " + this.soil_to_fertilizer_map);
        System.out.println("fertilizer_to_water_map: " + this.fertilizer_to_water_map);
        System.out.println("water_to_light_map: " + this.water_to_light_map);
        System.out.println("light_to_temperature_map: " + this.light_to_temperature_map);
        System.out.println("temperature_to_humidity_map: " + this.temperature_to_humidity_map);
        System.out.println("humidity_to_location_map: " + this.humidity_to_location_map);
    }

}
