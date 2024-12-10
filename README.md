# Advertisement Placement Tool

## Project Overview

The Advertisement Placement Tool our group created is made to help companies strategically place advertisements by identifying the most cost-effective locations. Using publicly available data from 25 major U.S. cities, the tool calculates Audience Reach, Demographic Fit Score, and Cost Efficiency Score. Users can customize inputs like age range, income, employed percentage, and budget, and the program recommends optimal locations based on these criteria. The results include a ranked list of cities, budget allocations, and a visual representation of cost efficiency.

## Files in Repository

1. **`main.py`**: Python program implementing all features of the tool.
2. **`demographics.csv`**: Sample data file our group did research on to create with city-specific information that will be used to assign optimal locations for the user. 
3. **`requirements.txt`**: Lists Python libraries required for the program.
4. **`README.md`**: This file, explaining our project and examples on how to use it. 


## How to Run the Program

### Run the program with your chosen parameters:
   ```bash
   python3 main.py --budget <TOTAL_BUDGET> --age <AGE_RANGE> --income <INCOME_RANGE> --employedpercentage <EMPLOYED_PERCENTAGE> --top_num <NUMBER_OF_LOCATIONS>
   ```
   Example we used in our presentation which is the company Apples target market:
   ```bash
   python3 main.py --budget 50000 --age 25-35 --income 75000-120000 --employedpercentage 20 --top_num 3
   ```


## Outputs

1. **Ranked Locations**: A prioritized list of cities based on cost efficiency.
2. **Budget Allocation**: A detailed breakdown of the budget assigned to each top location.
3. **Visualizations**: A bar chart of cost efficiency scores and their locations.
4. **Exported Report**: A summary of results and budget allocations.



## Methodology

## 1. **Audience Reach**:
Audience Reach is a measure of how many people are likely to see an ad at a certain location. It depends on three things: foot traffic (how many people pass by the location), the employed population (how many people in the area have jobs and may have money to spend), and the total population of the area. The formula to calculate audience reach is:

### Audience Reach = Foot Traffic × (Employed Population / Total Population)
This gives you an estimate of how many people in the area are likely to see the ad based on these factors. 

## 2. **Cost Efficiency Score**:
Cost Efficiency Score shows how well a location gives you exposure for the money you spend. It answers the question: “How many people will see my ad for each dollar I spend?” A higher score means you're getting more exposure for your money.
### Cost Efficiency Score = Audience Reach / Ad Cost
This tells you how cost-effective the location is for reaching people.
The budget is split based on each location's Cost Efficiency Score. To decide how much money each location gets, we first calculate the total Cost Efficiency Score for all the selected locations. Then, each location receives a portion of the budget that corresponds to its share of the total score. Locations with higher scores get a larger portion of the budget, while those with lower scores receive less. For example, if two locations have scores of 4 and 6, the total score is 10. The first location would get 40% of the total budget, and the second location would get 60%. This way, the budget is allocated more efficiently, giving more money to locations that are considered better at reaching the target audience for the cost.

## 3. **Budget Allocation**:
Budgets are allocated proportionally to the cost efficiency score of each location:
Allocated Budget = cost_efficiency_score / total_efficiency_score * total_budget


## Attribute Table

| **Method/Function**            | **Primary Author** | **Techniques Demonstrated**                |
|--------------------------------|--------------------|--------------------------------------------|
| `Demographic.__init__`         | Lynell             | Attribute initialization                  |
| `Demographic.load_demographics`| Lynell             | `with` statements                         |
| `Demographic.filter_locations` | Lynell             | Generator expressions                     |
| `Ranker.__init__`              | Prince             |                                           |
| `Ranker.add_location`          | Prince             | Optional parameters                       |
| `Ranker.audience_reach`        | Prince             | Mathematical calculations                 |
| `Ranker.cost_efficiency_score` | Prince             | Use of a key function (`lambda`, `sorted`)|
| `Ranker.rank_locations`        | Prince             |                                           |
| `Budget.__init__`              | Meanna             | Attribute initialization                  |
| `Budget.allocate_budget`       | Meanna             | List comprehensions                       |
| `Budget.optimal_spending`      | Meanna             | Attribute assignment                      |
| `Budget.adjust_budget_allocation` | Meanna          | Iteration with conditionals               |
| `Budget.track_spending`        | Meanna             |                                           |
| `UserInterface.__init__`       | Nabil              | Composition of classes                    |
| `UserInterface.parse_args`     | Nabil              | ArgumentParser class                      |
| `UserInterface.run`            | Nabil              | Command flow orchestration                |
| `UserInterface.display_results`| Jasmine            | `f-strings` containing expressions        |
| `UserInterface.display_bar_chart` | Jasmine         | Data visualization with `matplotlib`      |
| `UserInterface.save_results_to_file` | Jasmine       | File handling, formatted file output      | 

## References

### Annotated Bibliography

**Data USA. (n.d.). City Information.** Retrieved from [https://datausa.io/](https://datausa.io/)  
This resource provides detailed demographic, economic, and social data for cities across the United States. The data was used in this project to analyze various metrics such as population, age, and income distribution for effective advertising placement. Its user-friendly interface and visualization tools made it easy to identify key characteristics for our target audience.

**Alluvit Media. (n.d.). Billboard Advertising Costs.** Retrieved from [https://www.alluvitmedia.com/billboard-advertising.php](https://www.alluvitmedia.com/billboard-advertising.php)  
This website offers insights into billboard advertising costs across different locations in the U.S. It provided the monthly billboard ad cost data required to calculate cost efficiency scores for various cities. The information was instrumental in determining the financial feasibility of advertising campaigns in specific regions.

**Unacast. (n.d.). Foot Traffic Data.** Retrieved from [https://www.unacast.com/](https://www.unacast.com/)  
Unacast aggregates foot traffic data by analyzing movement patterns in specific locations using advanced sensors and tracking technologies. This data was critical in estimating audience reach for each location by providing insights into the volume of people passing through billboard areas. It helped refine our calculations for determining the effectiveness of potential advertising sites.

**World Population Review. (n.d.). US Cities by Population.** Retrieved from [https://worldpopulationreview.com/us-cities](https://worldpopulationreview.com/us-cities)  
This source provides up-to-date population statistics for cities across the United States. It was utilized to select the most populous cities as the focus of the project, ensuring the data used represented areas with significant advertising potential. The resource also supported calculations for metrics like employed population percentages.

## Key Features:
- **Customizable Inputs**: Users can set specific demographic and budget preferences.
- **Dynamic Rankings**: Locations are evaluated using real-world data and prioritized by cost efficiency.
- **Clear Visualizations**: A bar chart and summary file make results easy to interpret and share.
