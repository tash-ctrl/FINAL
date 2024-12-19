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

_Image Placeholder: Add generated image of party representation line chart._

### 2. Nominate Dimensional Analysis
- **Description:** Visualizes ideological scores (nominate dimensions) for members of the House and Senate.
- **Visualization:** A scatter plot with points color-coded for the House and Senate.

_Image Placeholder: Add generated image of nominate dimensional scatter plot._

### 3. Geographic Distribution
- **Description:** Highlights the number of congressional members from each state.
- **Visualization:** A bar chart displaying state-wise representation.

_Image Placeholder: Add generated image of geographic distribution bar chart._

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

