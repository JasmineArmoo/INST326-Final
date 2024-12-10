# Advertisement Placement Tool

## Project Overview

The **Advertisement Placement Tool** is designed to help companies strategically place billboard advertisements by identifying the most cost-effective locations. Using publicly available data from 25 major U.S. cities, the tool calculates metrics such as **Audience Reach**, **Demographic Fit Score**, and **Cost Efficiency Score**. Users can customize inputs like age range, income, employed percentage, and budget, and the program recommends optimal locations based on these criteria. The results include a ranked list of cities, budget allocations, and a visual representation of cost efficiency.

This project demonstrates the practical application of data analysis and budget optimization techniques, offering a streamlined solution for improving advertising strategies.

---

## Files in Repository

1. **`main.py`**: Core Python program implementing all features of the tool.
2. **`demographics.csv`**: Sample data file our group created with city-specific information.
3. **`requirements.txt`**: Lists Python libraries required for the program.
4. **`README.md`**: Documentation explaining the project and how to use it.

---

## How to Run the Program

1. Clone the repository:
   ```bash
   git clone https://github.com/YourRepo/advertisement-placement-tool.git
   ```
2. Navigate to the directory:
   ```bash
   cd advertisement-placement-tool
   ```
3. Install required libraries:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the program with your chosen parameters:
   ```bash
   python3 main.py --budget <TOTAL_BUDGET> --age <AGE_RANGE> --income <INCOME_RANGE> --employedpercentage <EMPLOYED_PERCENTAGE> --top_num <NUMBER_OF_LOCATIONS>
   ```
   Example:
   ```bash
   python3 main.py --budget 10000 --age 25-35 --income 50000-80000 --employedpercentage 20 --top_num 5
   ```

---

## Outputs

1. **Ranked Locations**: A prioritized list of cities based on cost efficiency.
2. **Budget Allocation**: A detailed breakdown of the budget assigned to each top location.
3. **Visualizations**: A bar chart of cost efficiency scores (`advertising_chart.png`).
4. **Exported Report**: A summary of results and budget allocations (`advertising_results.txt`).

---

## Methodology

### 1. **Audience Reach**:
\[
\text{Audience Reach} = \text{Foot Traffic} \times \left( \frac{\text{Employed Population}}{\text{Total Population}} \right)
\]
This metric estimates how many people are likely to see an ad at a given location by combining movement data with demographic details.

### 2. **Cost Efficiency Score**:
\[
\text{Cost Efficiency Score} = \frac{\text{Audience Reach}}{\text{Ad Cost}}
\]
This score evaluates the cost-effectiveness of each location, helping prioritize those with the best value.

### 3. **Budget Allocation**:
Budgets are allocated proportionally to the cost efficiency score of each location:
\[
\text{Allocated Budget} = \left( \frac{\text{Location's Cost Efficiency Score}}{\text{Total Cost Efficiency Score}} \right) \times \text{Total Budget}
\]

---

## Attribution Table

| Method/Function          | Primary Author  | Techniques Demonstrated                     |
|---------------------------|-----------------|---------------------------------------------|
| `Demographic.load_demographics` | Lynell         | with statements, filtering                 |
| `Demographic.filter_locations`  | Lynell         | comprehensions, sequence unpacking         |
| `Ranker.add_location`     | Prince          | keyword arguments, f-strings               |
| `Ranker.rank_locations`   | Prince          | key function with sorted()                 |
| `Budget.allocate_budget`  | Meanna          | comprehensions, calculation logic          |
| `Budget.track_spending`   | Meanna          | f-strings, calculations with totals        |
| `UserInterface.parse_args`| Nabil           | ArgumentParser class, validation functions |
| `UserInterface.run`       | Nabil           | composition of classes                     |
| `UserInterface.display_results`| Jasmine      | visualizing with pyplot, formatting output |
| `UserInterface.save_results_to_file`| Jasmine | file handling, formatted output            |

---

## Data Sources

1. **City Information**: [Data USA](https://datausa.io/)
2. **Billboard Ad Costs**: [Alluvit Media](https://www.alluvitmedia.com/billboard-advertising.php)
3. **Foot Traffic**: [Unacast](https://www.unacast.com/)
4. **Population Statistics**: [World Population Review](https://worldpopulationreview.com/us-cities)

We selected the most populous cities in the U.S. with publicly available data on population, foot traffic, billboard ad costs, and employment statistics to ensure the tool provides robust, accurate insights.

---

## Key Features:
- **Customizable Inputs**: Users can set specific demographic and budget preferences.
- **Dynamic Rankings**: Locations are evaluated using real-world data and prioritized by cost efficiency.
- **Clear Visualizations**: A bar chart and summary file make results easy to interpret and share.

This project reflects our ability to design innovative, data-driven solutions for real-world challenges, using Python programming principles and teamwork to deliver a cohesive and functional tool.
