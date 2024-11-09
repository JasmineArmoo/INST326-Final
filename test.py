#1 Lynell

#2 Prince

class DemographicAnalyzer:
 	def __init__(self):
       
  	def analyze_data(self):
    
    ...
        

#3 Meanna

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
    def __init__(self):
        self.args = self.parse_args()
        self.budget = self.args.budget
        self.target_age_range = self.args.age
        self.target_income_range = self.args.income
        self.target_education = self.args.education
        self.top_n = self.args.top_n
        

if __name__ == "__main__":
    main()
    
    
import argparse
