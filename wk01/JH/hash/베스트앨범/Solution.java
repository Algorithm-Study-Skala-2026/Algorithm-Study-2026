package wk01.JH.hash.베스트앨범;

import java.util.*;

class Solution {
    public int[] solution(String[] genres, int[] plays) {
        HashMap<String, Integer> genreTotalPlays = new HashMap<>(); 
        HashMap<String, List<int[]>> genreSongs = new HashMap<>();

        for (int i = 0; i < genres.length; i++) {
            String genre = genres[i];
            int playCount = plays[i];

            genreTotalPlays.put(genre, genreTotalPlays.getOrDefault(genre, 0) + playCount);

            genreSongs.computeIfAbsent(genre, k -> new ArrayList<>());
            genreSongs.get(genre).add(new int[]{i, playCount}); 
        }

        List<String> sortedGenres = new ArrayList<>(genreTotalPlays.keySet());
        sortedGenres.sort((a, b) -> genreTotalPlays.get(b) - genreTotalPlays.get(a));

        List<Integer> result = new ArrayList<>();

        for (String genre : sortedGenres) {
            List<int[]> songs = genreSongs.get(genre);

            songs.sort((a, b) -> {
                if (b[1] != a[1]) return b[1] - a[1];
                return a[0] - b[0];
            });

            for (int i = 0; i < Math.min(2, songs.size()); i++) {
                result.add(songs.get(i)[0]);
            }
        }

        return result.stream().mapToInt(i -> i).toArray();
    }
}
