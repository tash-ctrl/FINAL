import sys
import os
sys.path.insert(0, os.path.join(os.getcwd(), 'src'))

from api_handler import ProPublicaAPI
from politician import Politician
from investment_tracker import InvestmentTracker
from visualizer import PortfolioVisualizer

def main():
    # Initialize ProPublica API
    propublica_api = ProPublicaAPI()

    # Fetch politicians' data
    representatives_data = propublica_api.get_representatives()

    # Process politicians
    politicians = [
        Politician(
            name=rep.get('name', 'Unknown'),
            state=rep.get('state', 'Unknown'),
            party=rep.get('party', 'Unknown'),
            contributions=[]
        )
        for rep in representatives_data if 'name' in rep
    ]

    # Analyze contributions
    investment_tracker = InvestmentTracker()
    for politician in politicians:
        investment_tracker.analyze_contributions(politician)

    # Visualize contributions
    PortfolioVisualizer.plot_contributions(politicians)

if __name__ == "__main__":
    main()