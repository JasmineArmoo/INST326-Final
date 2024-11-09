#1 Lynell
class DataLoader:
    def __init__(self):
        self.demographics = self.load_demographics('demographics.csv')
        self.resources = self.load_resources('resources.csv')
        self.costs = self.load_costs('costs.csv')
        self.profits = self.load_profits('profits.csv')

    def load_demographics(self, filename):
        data = {}
        try:
            with open(filename, 'r') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    data[row['Location']] = {
                        'age': int(row['Age']),
                        'income': int(row['Income'])
                    }
            return data
        except FileNotFoundError:
            print(f"Error: File {filename} not found.")
            return {}

#2 Prince

class DemographicAnalyzer:
   

    def __init__(self, demographics):
        self.demographics = demographics

    def filter_locations(self, target_age_range, target_income_range, min_education_level=None):
        return [
            location for location, info in self.demographics.items()
            if info['age'] in target_age_range and info['income'] in target_income_range and
            (min_education_level is None or info.get('education', 0) >= min_education_level)
        ]

        

#3 Meanna

class ResourceEvaluator:
    def __init__(self, location_data):
        """
        Initializes with location data.
        
        :param location_data: Dictionary with location scores.
        """
        self.location_name = location_data['location_name']
        self.infrastructure_score = location_data['infrastructure_score']
        self.media_reach_score = location_data['media_reach_score']
        self.other_factors_score = location_data['other_factors_score']

    def evaluate_resources(self):
        """
        Calculates the total resource score.

        :return: Total resource score.
        """
        return self.infrastructure_score + self.media_reach_score + self.other_factors_score

#4 Nabil

class LocationProfitability:
    def __init__(self, location_name, ad_cost, projected_revenue, demographic_score, media_reach_score):
        self.location_name = location_name
        self.ad_cost = ad_cost
        self.projected_revenue = projected_revenue
        self.demographic_score = demographic_score
        self.media_reach_score = media_reach_score
        self.profitability_score = self.calculate_profitability()
    
    def calculate_roi(self):
        """Calculates the return on investment (ROI) for this location."""
        return (self.projected_revenue - self.ad_cost) / self.ad_cost
    


#5 Jasmine
class UserInterface: 
    """ Controls user input, location, and creates visualization from data
   
    Attributes:
    budget (float): the available budget a company has for an ad
    locations (list): the locations for analysis
    """
    def __init__(self, budget, location_data):
        self.budget = budget
        
        self.location_data = location_data
        

if __name__ == "__main__":
    main()
    
import argparse
