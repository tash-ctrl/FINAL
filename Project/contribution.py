import sys
import os
sys.path.insert(0, os.path.join(os.getcwd(), 'src'))

from api_handler import ContributionAPI
from politician import Politician
from investment_tracker import InvestmentTracker
from visualizer import PortfolioVisualizer

def main():
    # Initialize Contribution API
    contribution_api = ContributionAPI()

    # Fetch contributions data
    contributions_data = contribution_api.get_contributions()

    # Process politicians from contributions
    politicians = [
        Politician(
            name=f"Politician {i}",
            state="Unknown",
            party="Unknown",
            contributions=data
        )
        for i, data in enumerate(contributions_data.values())
    ]

    # Analyze contributions
    investment_tracker = InvestmentTracker()
    for politician in politicians:
        investment_tracker.analyze_contributions(politician)

    # Visualize contributions
    PortfolioVisualizer.plot_contributions(politicians)

if __name__ == "__main__":
    main()

# Supporting Modules in src Folder

# File: src/api_handler.py

import requests

class ProPublicaAPI:
    def __init__(self):
        self.base_url = "https://projects.propublica.org/represent/members.json"

    def get_representatives(self):
        try:
            response = requests.get(self.base_url)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            print(f"Error fetching data from ProPublica API: {e}")
            return []

class ContributionAPI:
    def __init__(self):
        self.base_url = "https://www.fec.gov/data/candidates"

    def get_contributions(self):
        try:
            response = requests.get(self.base_url)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            print(f"Error fetching data from FEC API: {e}")
            return {}

# File: src/politician.py

class Politician:
    def __init__(self, name, state, party, contributions):
        self.name = name
        self.state = state
        self.party = party
        self.contributions = contributions

    def to_dict(self):
        return {
            "name": self.name,
            "state": self.state,
            "party": self.party,
            "contributions": self.contributions
        }

# File: src/investment_tracker.py

class InvestmentTracker:
    def analyze_contributions(self, politician):
        politician.contribution_total = sum(contribution.get('amount', 0) for contribution in politician.contributions)

# File: src/visualizer.py

import matplotlib.pyplot as plt

class PortfolioVisualizer:
    @staticmethod
    def plot_contributions(politicians):
        names = [p.name for p in politicians]
        totals = [getattr(p, 'contribution_total', 0) for p in politicians]

        plt.figure(figsize=(10, 6))
        plt.bar(names, totals)
        plt.title("Total Contributions by Politician")
        plt.xlabel("Politicians")
        plt.ylabel("Total Contributions ($)")
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()
