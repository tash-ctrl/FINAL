# Politicians' Investment Analysis and Polarization Visualizations

## Project Description
This project aims to analyze political data from two perspectives:
1. **Historical Congressional Data:** Visualizing trends, ideological distributions, and geographic representation in the U.S. Congress using provided datasets.
2. **Investment Analysis:** Leveraging APIs to analyze financial contributions and trends among politicians.

The project uses:
- **ProPublica API:** To fetch data on representatives and their attributes.
- **Contribution API:** To analyze political contributions.
- **Dataset:** "US History All House and Senate Members" for historical analysis.

### Features
- Three branches:
  1. **OOP with ProPublica API**
  2. **CSV-based analysis using Jupyter Notebook**
  3. **Contribution API analysis**
- Modular codebase with clear OOP design principles.
- Visualizations illustrating political trends, ideologies, and geographic distribution.

---

## Visualizations

### 1. Party Representation Over Time
- **Description:** Tracks the number of members in Congress by party over sessions.
- **Visualization:** A line chart showing trends across Congress sessions.

<img width="798" alt="Screen Shot 2024-12-18 at 10 24 39 PM" src="https://github.com/user-attachments/assets/c9d818cc-4ed3-4b16-b1f0-ff8cdf6fedc0" />


### 2. Nominate Dimensional Analysis
- **Description:** Visualizes ideological scores (nominate dimensions) for members of the House and Senate.
- **Visualization:** A scatter plot with points color-coded for the House and Senate.

<img width="802" alt="Screen Shot 2024-12-18 at 10 24 14 PM" src="https://github.com/user-attachments/assets/ee5e940a-9f22-4beb-a215-5c8a6540c8d8" />


### 3. Geographic Distribution
- **Description:** Highlights the number of congressional members from each state.
- **Visualization:** A bar chart displaying state-wise representation.
<img width="802" alt="Screen Shot 2024-12-18 at 10 21 50 PM" src="https://github.com/user-attachments/assets/63ac5885-b816-45d6-a598-c783d4bf000a" />

**The goal of this project is to analyze political data to understand historical and current trends in U.S. congressional representation, financial contributions, and ideological patterns. The project addresses this by integrating data from multiple sources, including APIs and historical datasets, while leveraging object-oriented programming (OOP) principles to ensure a structured and reusable codebase.
---

## Installation

### Prerequisites
- Python 3.8+
- Libraries: `pandas`, `matplotlib`, `requests`

### Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/your-repo/politicians-analysis.git
   cd politicians-analysis
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Place your API keys (if needed) in a `.env` file:
   ```
   PROPUBLICA_API_KEY=your_propublica_api_key
   CONTRIBUTION_API_KEY=your_contribution_api_key
   ```

---

## How to Run

### 1. OOP with ProPublica API
Run the OOP-focused script:
```bash
python main_oop.py
```
- Fetches representative data from ProPublica API.
- Processes and visualizes contributions using OOP principles.

### 2. CSV-Based Analysis
Run the Jupyter Notebook for polarization visualizations:
```bash
jupyter notebook analysis.ipynb
```
- Analyzes the provided "US History All House and Senate Members" dataset.
- Generates line, scatter, and bar charts.

### 3. Contribution API Analysis
Run the contribution-focused script:
```bash
python main_contribution.py
```
- Fetches contribution data from the Contribution API.
- Visualizes financial trends among politicians.


---

## Acknowledgments
- ProPublica API for representative data.
- Contribution API for political contribution data.
- Provided dataset for historical congressional analysis.

---

## License
This project is licensed under the MIT License.

