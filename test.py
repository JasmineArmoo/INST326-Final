#1 Lynell

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