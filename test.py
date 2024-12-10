import json
import argparse
import matplotlib.pyplot as plt

class Demographic:
    """
    A class for loading and analyzing demographic data from a JSON file.

    Attributes:
        demographics (dict): Dictionary containing demographic data for different locations.

    Methods:
        - load_demographics: Loads demographic data from a JSON file into a dictionary.
        - filter_locations: Filters locations based on age, income, and employment criteria.

    Author: Lynell 
    """

    def __init__(self, filename):
        """
        Initializes the Demographic object and loads demographic data from the specified file.

        Args:
            filename (str): The path to the JSON file containing demographic data.

        Author: Lynell
        """
        self.demographics = self.load_demographics(filename)

    def load_demographics(self, filename):
        """
        Loads demographic data from a JSON file into a dictionary.

        Opens the JSON file and parses its content. Handles errors such as missing files or invalid JSON formatting.

        Args:
            filename (str): The path to the JSON file.

        Returns:
            dict: A dictionary with location names as keys and demographic information as values. Returns an empty dictionary if the file is missing or invalid.

        Techniques:
            - use of json.load()

        Author: Lynell
        """
        try:
            with open(filename, "r") as file:
                return json.load(file)
        except FileNotFoundError:
            print(f"Error: File {filename} not found.")
            return {}
        except json.JSONDecodeError:
            print(f"Error: File {filename} is not a valid JSON file.")
            return {}

    def filter_locations(self, target_age_range=None, target_income_range=None, min_employed_percentage=None):
        """
        Filters locations based on the provided demographic criteria.

        Applies conditional filters to demographic data. Locations are filtered by age range, income range, and minimum employed population percentage. If no criteria are provided, all locations are returned.

        Args:
            target_age_range (range): Target age range of demographic.
            target_income_range (range): Target income range of demographic.
            min_employed_percentage (float): Minimum employed population percentage (0-100).

        Returns:
            list: A list of location names that meet the criteria. Returns all locations if no filters are applied.
            
        Techniques:
            - condtional expressions
            
        Author: Lynell
        """
        if not any([target_age_range, target_income_range, min_employed_percentage]):
            return list(self.demographics.keys())

        return [
            location for location, info in self.demographics.items()
            if (target_age_range is None or int(info["age"]) in target_age_range) and
               (target_income_range is None or int(info["income"]) in target_income_range) and
               (min_employed_percentage is None or (info["employedpopulation"] / info["population"]) * 100 >= min_employed_percentage)
        ]
        
class Ranker:
   """
   A class used to evaluate and rank advertising locations based on cost efficiency and audience reach.

   This class helps businesses identify the most cost-effective locations to place ads by calculating metrics
   like audience reach and cost efficiency. Locations are ranked based on their ability to reach an audience
   relative to the ad cost, enabling optimized ad spend allocation.

   Attributes:
       locations (list): A list that holds dictionaries, each containing location details such as ad cost,
                         audience reach, and cost efficiency score.

   Author: Prince Osei
   """

   def __init__(self):
       """
       Initializes the Ranker instance.

       This method creates an empty list to store the evaluated location data, which includes location name,
       ad cost, audience reach, and cost efficiency score.

       Side effects:
           Initializes the locations attribute as an empty list.

       Author: Prince Osei
       """
       self.locations = []

   def add_location(self, location_name, ad_cost, foottraffic, employedpopulation, population):
       """
       Adds a location with its calculated audience reach and cost efficiency score to the list of locations.

       This method calculates the audience reach based on foot traffic, employed population, and the total
       population, and then computes the cost efficiency score based on the audience reach and the ad cost.

       Args:
           location_name (str): The name of the location being evaluated.
           ad_cost (float): The cost of running an advertisement in the location.
           foottraffic (int): The foot traffic data representing the number of people passing through the location.
           employedpopulation (int): The number of employed individuals in the location.
           population (int): The total population of the location.

       Side effects:
           Adds a dictionary representing the location to the locations list.

       Author: Prince Osei
       """
       audience_reach = self.audience_reach(foottraffic, employedpopulation, population)
       cost_efficiency_score = self.cost_efficiency_score(audience_reach, ad_cost)

       self.locations.append({
           "location_name": location_name,
           "ad_cost": ad_cost,
           "audience_reach": audience_reach,
           "cost_efficiency_score": cost_efficiency_score
       })

   def audience_reach(self, foottraffic, employedpopulation, population):
       """
       Calculates the audience reach for a location based on foot traffic, employed population, and total population.

       Audience reach is estimated by multiplying foot traffic by the proportion of employed individuals in the
       total population, which provides an estimate of the effective reach of advertisements in that location.

       Args:
           foottraffic (int): The number of people passing through the location.
           employedpopulation (int): The number of employed individuals in the location.
           population (int): The total population of the location.

       Returns:
           int: The calculated audience reach for the location.

       Author: Prince Osei
       """
       return round(foottraffic * (employedpopulation / population))


   def cost_efficiency_score(self, audience_reach, ad_cost):
       """
       Calculates the cost efficiency score for a location by dividing audience reach by ad cost.

       The cost efficiency score is a metric that evaluates how well a location can reach its audience relative
       to the cost of the advertisement. A higher score indicates a more cost-effective location for ad placement.

       Args:
           audience_reach (int): The calculated audience reach for the location.
           ad_cost (float): The cost of running an ad in the location.

       Returns:
           float: The cost efficiency score for the location.

       Author: Prince Osei
       """
       if ad_cost == 0:
           return 0
       return audience_reach / ad_cost

   def rank_locations(self, top_num=24):
       """
        Ranks the locations based on their cost efficiency scores and returns the top top_num locations.

       Locations are sorted in descending order of their cost efficiency scores, with the most cost-effective
       locations appearing first. This allows businesses to allocate their advertising budget to the locations
       that will generate the highest audience reach per dollar spent.

       Args:
           top_num (int): The number of top locations to return based on cost efficiency scores. Default is 24.

       Returns:
           list: A list of dictionaries representing the top-ranked locations based on their cost efficiency scores.

       Author: Prince Osei
      
       Techniques:
           - use of a key function (lambda, sorted)
           - optional parameters/keyword arguments

       """
       return sorted(self.locations, key=lambda loc: loc["cost_efficiency_score"], reverse=True)[:top_num]
   
   def get_average(self, demographics, filtered_locations):
    """
    Calculates and returns the average values for age, income, and employed population 
    for a list of filtered locations.

    Args:
        demographics (dict): Demographic data for locations.
        filtered_locations (list): List of locations to analyze.

    Returns:
        dict: A dictionary containing the averages for age, income, and employedpercentage.
              Returns 0 for each if no filtered locations are provided.
              
    Author: Prince Osei
    """
    if not filtered_locations:
        print("No filtered locations provided.")
        return {"age": 0, "income": 0, "employedpercentage": 0}

    total_age = sum([demographics[loc]["age"] for loc in filtered_locations])
    total_income = sum([demographics[loc]["income"] for loc in filtered_locations])
    total_employed_percentage = sum([
        (demographics[loc]["employedpopulation"] / demographics[loc]["population"]) * 100
        for loc in filtered_locations
    ])

    count = len(filtered_locations)

    return {
        "age": total_age / count,
        "income": total_income / count,
        "employedpercentage": total_employed_percentage / count
    }
    
class Budget:
    """
    Handles budget allocation for advertising locations based on cost efficiency scores.

    This class calculates how to distribute the budget proportionally across top locations, 
    tracks total spending, and allows for manual adjustments to allocations. It ensures the 
    budget is allocated effectively to maximize advertising impact.

    Author: Meanna
    """

    def __init__(self, total_budget, top_locations):
        """
        Initializes the Budget class with the total budget and top-ranked locations.

        Args:
            total_budget (float): The total amount of money available to allocate.
            top_locations (list): A list of dictionaries with location details and cost efficiency scores.

        Attributes:
            total_budget (float): Stores the total budget for allocation.
            top_locations (list): Holds the list of top locations with budget allocations and scores.

        Side Effects:
            Initializes the total_budget and top_locations attributes for the class.

        Author: Meanna
        """
        self.total_budget = total_budget
        self.top_locations = top_locations

    def allocate_budget(self):
        """
        Allocates the total budget across locations based on their cost efficiency scores.

        Side Effects:
            Modifies the top_locations list by adding an allocated_budget key for each location.

        Raises:
            ValueError: If no valid cost efficiency scores are available (total score is 0).

        Techniques:
            - f-strings containing expressions
            
        Author: Meanna
        """
        total_efficiency_score = sum([loc["cost_efficiency_score"] for loc in self.top_locations])
        if total_efficiency_score == 0:
            print("Error: No valid cost efficiency score. Cannot allocate budget.")
            return
        for loc in self.top_locations:
            loc["allocated_budget"] = (loc["cost_efficiency_score"] / total_efficiency_score) * self.total_budget

    def adjust_budget_allocation(self, location_name, new_budget):
        """
        Allows the user to adjust the budget for a specific location.

        Args:
            location_name (str): The name of the location to adjust.
            new_budget (float): The new budget value to assign to the specified location.

        Side Effects:
            Updates the allocated_budget value for the specified location in the top_locations list.

        Author: Meanna
        """
        for loc in self.top_locations:
            if loc["location_name"] == location_name:
                loc["allocated_budget"] = new_budget

    def optimal_spending(self):
        """
        Marks the allocated budget for each location as its optimal spending.

        Side Effects:
            Adds an optimal_spending key to each location in the top_locations list.

        Author: Meanna
        """
        for loc in self.top_locations:
            loc["optimal_spending"] = loc["allocated_budget"]

    def track_spending(self):
        """
        Tracks and summarizes the total spending and remaining budget.

        Side Effects:
            Prints a detailed summary of allocated budgets, the total budget, and any remaining funds.

        Techniques:
            - comprehensions
            
        Author: Meanna
        """
        total_spent = sum([loc["allocated_budget"] for loc in self.top_locations])
        remaining_budget = self.total_budget - total_spent
        print("\nBudget Allocation:")
        print(f"Total Budget: ${self.total_budget:.2f}")
        for loc in self.top_locations:
            print(f"{loc['location_name']}: Allocated Budget: ${loc['allocated_budget']:.2f}")
        print(f"Remaining Budget: ${remaining_budget:.2f}")

class UserInterface:
    """
    This class manages the user interface and coordinates the workflow of the advertising placement program.
    It parses user input, filters data, ranks locations, optimizes budgets, and outputs results.
    """

    def __init__(self):
        """
        This method initializes the UserInterface instance by parsing command-line arguments.

        Args:
            None

        Attributes:
            args (argparse.Namespace): Parsed command-line arguments, it contains inputs such as budget,
                                       target demographics, and file paths.

        Returns:
            None
            
        Author: Nabil Habona
        """
        self.args = self.parse_args()

    def parse_args(self):
        """
        This method parses command-line arguments to configure the program's behavior.

        Args:
            None

        Returns:
            argparse.Namespace: A namespace object that contains parsed arguments, such as budget, age range,
                                income range, employed population percentage, number of top locations, and
                                the demographics data file.

        Side effects:
            It will raise a argparse.ArgumentTypeError if the input range format is invalid.
            
        Author: Nabil Habona
        Techniques: the ArgumentParser class from the argparse module
        """
        def parse_range(value):
            try:
                start, end = map(int, value.split('-'))
                if start > end:
                    raise argparse.ArgumentTypeError(f"Invalid range: {value}")
                return range(start, end + 1)
            except ValueError:
                raise argparse.ArgumentTypeError(f"Invalid range format: {value}")

        parser = argparse.ArgumentParser(description="Strategic Advertising Placement Tool")
        parser.add_argument("--budget", type=int, required=True, help="Total advertising budget")
        parser.add_argument("--age", type=parse_range, help="Target age range (e.g., 25-35)")
        parser.add_argument("--income", type=parse_range, help="Target income range (e.g., 50000-80000)")
        parser.add_argument("--employedpercentage", type=float, help="Minimum employed population percentage (optional)")
        parser.add_argument("--top_num", type=int, default=24, help="Number of top locations to display")
        parser.add_argument("--demographics", type=str, default="demographics.json", help="Demographics data file")
        return parser.parse_args()

    def check_budget(self, budget):
        """
        Validates the budget input to ensure it is a positive number and of the correct type.

        Args:
            budget (str, int, float): The user's input for the advertising budget.

        Returns:
            bool: True if the budget is valid 
            
        Raises: 
            ValueError otherwise.
            
        Author: Prince
        """
        if isinstance(budget, str):
            budget = budget.strip().replace(",", "")
            try:
                budget = float(budget)
            except ValueError:
                raise ValueError(f"Invalid budget format: '{budget}'. Please enter a valid numeric value.")

        if not isinstance(budget, (int, float)) or budget <= 0:
            raise ValueError("Budget must be a positive number.")

        return True
    
    def run(self):
        """
        This method executes the program's main workflow, integrating various components.
        First, checks the budget and loads the demographic data. Then, it filters the locations based on user-defined criteria, such as age range, income range, and employed percentage. 
        Next, it ranks the locations based on cost efficiency. After ranking, it allocates budgets for the top locations. 
        Finally, it displays the results, generates visualizations, and saves outputs to files.

        Args:
            None

        Returns:
            None

        Side effects:
            It will displays results in the console, generates a bar chart, and saves outputs to files.
            
        Author: Nabil Habona
        Techniques: Composition
        """
        self.check_budget(self.args.budget)
        
        analyzer = Demographic(self.args.demographics)

        target_age_range = self.args.age
        target_income_range = self.args.income
        min_employed_percentage = self.args.employedpercentage

        filtered_locations = analyzer.filter_locations(
            target_age_range=target_age_range,
            target_income_range=target_income_range,
            min_employed_percentage=min_employed_percentage
        )

        ranker = Ranker()
        for location in filtered_locations:
            data = analyzer.demographics[location]
            ranker.add_location(
                location_name=location,
                ad_cost=data["ad_cost"],
                foottraffic=data["foottraffic"],
                employedpopulation=data["employedpopulation"],
                population=data["population"],
            )

        top_locations = ranker.rank_locations(self.args.top_num)
        self.display_results(top_locations)

        averages = ranker.get_average(analyzer.demographics, filtered_locations)

        print(f"\nThe average age for the selected locations is: {averages['age']:.2f} years")
        print(f"The average income for the selected locations is: ${averages['income']:.2f}")
        print(f"The average employed percentage for the selected locations is: {averages['employedpercentage']:.2f}%")

        budget_optimizer = Budget(self.args.budget, top_locations)
        budget_optimizer.allocate_budget()
        budget_optimizer.optimal_spending()
        budget_optimizer.track_spending()

        self.display_bar_chart(top_locations)
        self.save_results_to_file(top_locations, budget_optimizer, averages)
       
    def display_results(self, top_locations):
       """ 
       Shows the largest advertising locations based off of its cost efficiency
       
       Args:
            top_locations (dictionary list): A lists of the highest ranked 
            locations and their features (name, reach, cost efficiency score)
       
       Side effects:
            Prints the best locations to console
       
       Author: Jasmine Armoo
       """
       print("Top Advertising Locations:\n")
       for loc in top_locations:
           print(f"Location: {loc['location_name']}, "
                 f"Cost Efficiency Score: {loc['cost_efficiency_score']:.2f}, "
                 f"Audience Reach: {loc['audience_reach']:.2f}")


    def display_bar_chart(self, top_locations):
       """
       Creates bar chart which shows the best advertising areas based off of 
       their cost efficiency score
       
       Args:
            top_locations (dictionary list):  A lists of the highest ranked 
            locations and their features that are going to be visualized
       
       Side effects:
            Creates a bar chart using with Matplotlib,and saves it as an 
            image file

       Author: Jasmine Armoo
       Technique: Visualizing data with pyplot
       """
       
       sorted_locations = sorted(top_locations, key=lambda loc: loc["cost_efficiency_score"], reverse=True)
       locations = [loc["location_name"] for loc in sorted_locations][::-1]
       efficiency_scores = [loc["cost_efficiency_score"] for loc in sorted_locations][::-1]
       plt.barh(locations, efficiency_scores)
       plt.title("Top Advertising Locations",fontsize=16)
       plt.xlabel("Cost Efficiency Score", fontsize=14)
       plt.tight_layout()


       plt.savefig("advertising_chart.png")
       print("\nGraph saved as advertising_chart.png")
      
       plt.show()

    def save_results_to_file(self, top_locations, budget_optimizer, averages):
       """
       Saves highest ranked locations and their budget allocations to text file
       
       Args:
            top_location (dictionary list): A lists of the highest ranked 
            locations and their features that are going to be visualized
            
            budget_optimizer (Budget): The budget object that tracks and
            allocates location budgets
            
        Side effects:
            Creates advertising_results.txt and writes to file
            
        Techniques:
            - with statements
            
        Author: Jasmine Armoo

       """
       with open("advertising_results.txt", "w") as file:
        file.write("Top Advertising Locations:\n")
        for loc in top_locations:
            file.write(f"Location: {loc['location_name']}, "
                       f"Cost Efficiency Score: {loc['cost_efficiency_score']:.2f}, "
                       f"Audience Reach: {loc['audience_reach']:.2f}\n")

        file.write("\nAverage Metrics:\n")
        file.write(f"Average Age: {averages['age']:.2f} years\n")
        file.write(f"Average Income: ${averages['income']:.2f}\n")
        file.write(f"Average Employed Percentage: {averages['employedpercentage']:.2f}%\n")
        
        file.write("\nBudget Allocation:\n")
        file.write(f"Total Budget: ${budget_optimizer.total_budget:.2f}\n")
        for loc in top_locations:
            file.write(f"{loc['location_name']}: Allocated Budget: ${loc['allocated_budget']:.2f}\n")
        remaining_budget = budget_optimizer.total_budget - sum([loc["allocated_budget"] for loc in top_locations])
        file.write(f"\nRemaining Budget: ${remaining_budget:.2f}\n")

        print("Results saved as advertising_results.txt")
        
if __name__ == "__main__":
   ui = UserInterface()
   ui.run()   
   