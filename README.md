# scraper_results

JSON output of our Brawl Stars API scrapper. Sorted by country of club.

## Current Modes:

### ```1v1```

Performs a direct comparasion of Brawlers, ignoring maps and modes. The first file that needs to be run is ```1v1_scoring.py```, which gives a JSON file that has a list of all battle times for eachThe function ```find_all_winrates(brawler_name, dataset)``` returns ```(number_of_wins, number_of_games_found)``` for the inputed brawler against all Brawlers that have a recorded game against the input brawler. The function ```best_for_three(brawler_array, dataset)``` returns a list of tuples that show the sum of the win rates for a potential brawler against the input array of three brawlers, sorted in decreasing order.


### ```1v1mode```

Preforms a comparassion of Brawlers, accounting for the gamemode. Current implementation of the results codebase only includes one function ```find_all_winrates(brawler_name, game_mode, dataset)```, which preforms the same as in the ```1v1``` mode.

